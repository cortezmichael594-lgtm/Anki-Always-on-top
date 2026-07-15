from __future__ import annotations

import ctypes
import shutil
import subprocess
import sys
import weakref
from typing import Any

from aqt import mw
from aqt.addcards import AddCards
from aqt.qt import QKeySequence, QShortcut, Qt
from aqt.utils import tooltip

from . import constants
from .settings import load_settings
from .strings import tr

_PLATFORM: str = (
    "win" if sys.platform.startswith("win")
    else "mac" if sys.platform.startswith("darwin")
    else "lin"
)

_HWND_TOPMOST = -1
_HWND_NOTOPMOST = -2
_SWP_NOMOVE = 0x0002
_SWP_NOSIZE = 0x0001
_SWP_NOACTIVATE = 0x0010

# ctypes expone tipos dinamicos de Windows sin firma estatica: Any es inevitable aqui.
_user32: Any
if _PLATFORM == "win":
    from ctypes import wintypes

    _user32 = ctypes.windll.user32  # type: ignore[attr-defined]
    _user32.SetWindowPos.restype = wintypes.BOOL
    _user32.SetWindowPos.argtypes = [
        wintypes.HWND, wintypes.HWND,
        ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int,
        wintypes.UINT,
    ]
else:
    _user32 = None


def _win_set_topmost(hwnd: int, topmost: bool) -> bool:
    if _user32 is None:
        return False
    try:
        insert_after = _HWND_TOPMOST if topmost else _HWND_NOTOPMOST
        ok = _user32.SetWindowPos(
            wintypes.HWND(hwnd),
            wintypes.HWND(insert_after),
            0, 0, 0, 0,
            _SWP_NOMOVE | _SWP_NOSIZE | _SWP_NOACTIVATE,
        )
        return bool(ok)
    except Exception as exc:
        print(f"[always_on_top] SetWindowPos: {exc!r}")
        return False


def _linux_reinforce_topmost(win_id: int, topmost: bool) -> None:
    if shutil.which("wmctrl") is None:
        return
    try:
        action = "add" if topmost else "remove"
        subprocess.run(
            ["wmctrl", "-i", "-r", f"0x{win_id:x}", "-b", f"{action},above"],
            check=False,
            timeout=1,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except Exception as exc:
        print(f"[always_on_top] wmctrl: {exc!r}")


class AlwaysOnTopManager:
    _STAY_ON_TOP: Qt.WindowType = Qt.WindowType.WindowStaysOnTopHint

    def __init__(self) -> None:
        self._enabled: bool = False
        self._current_add_cards: weakref.ReferenceType[AddCards] | None = None
        self._shortcut: QShortcut | None = None

    def start(self) -> None:
        self.apply_shortcut(load_settings().shortcut, notify=False)

    def apply_shortcut(self, shortcut: str, notify: bool) -> None:
        key_sequence = QKeySequence(shortcut)
        if key_sequence.isEmpty():
            key_sequence = QKeySequence(constants.DEFAULT_SHORTCUT)
        self._teardown_shortcut()
        self._shortcut = QShortcut(key_sequence, mw)
        self._shortcut.setContext(Qt.ShortcutContext.ApplicationShortcut)
        self._shortcut.activated.connect(self._on_shortcut_activated)
        if notify:
            tooltip(tr("shortcut_updated"), period=constants.TOOLTIP_PERIOD_MS)

    def on_config_updated(self, _new_config: dict[str, Any]) -> None:
        try:
            self.apply_shortcut(load_settings().shortcut, notify=True)
        except Exception as exc:
            print(f"[always_on_top] on_config_updated: {exc!r}")

    def on_add_cards_init(self, add_cards: AddCards) -> None:
        try:
            self._current_add_cards = weakref.ref(add_cards)
            if self._enabled:
                self._apply_hint(add_cards, True)
        except Exception as exc:
            print(f"[always_on_top] on_add_cards_init: {exc!r}")

    def _on_shortcut_activated(self) -> None:
        try:
            self._toggle()
        except Exception as exc:
            print(f"[always_on_top] toggle: {exc!r}")

    def _toggle(self) -> None:
        self._enabled = not self._enabled
        window = self._get_current_add_cards()
        if window is not None:
            self._apply_hint(window, self._enabled)
        tooltip(
            tr("on") if self._enabled else tr("off"),
            period=constants.TOOLTIP_PERIOD_MS,
        )

    def _get_current_add_cards(self) -> AddCards | None:
        if self._current_add_cards is None:
            return None
        return self._current_add_cards()

    def _apply_hint(self, window: AddCards, enabled: bool) -> None:
        try:
            if _PLATFORM == "win":
                self._apply_hint_native_win(window, enabled)
            else:
                self._apply_hint_qt_flags(window, enabled)
                if _PLATFORM == "lin":
                    _linux_reinforce_topmost(int(window.winId()), enabled)
        except RuntimeError:
            # La ventana de Qt pudo destruirse entre el weakref y esta llamada.
            pass

    def _apply_hint_native_win(self, window: AddCards, enabled: bool) -> None:
        hwnd = int(window.winId())
        if not _win_set_topmost(hwnd, enabled):
            self._apply_hint_qt_flags(window, enabled)

    def _apply_hint_qt_flags(self, window: AddCards, enabled: bool) -> None:
        flags = window.windowFlags()
        new_flags = flags | self._STAY_ON_TOP if enabled else flags & ~self._STAY_ON_TOP
        if new_flags == flags:
            return

        # Cambiar flags de ventana en Qt la oculta: hay que restaurar geometria y foco.
        was_visible = window.isVisible()
        was_active = window.isActiveWindow()
        geometry = window.geometry()

        window.setWindowFlags(new_flags)

        if was_visible:
            window.setGeometry(geometry)
            window.show()
            window.raise_()
            if was_active:
                window.activateWindow()

    def _teardown_shortcut(self) -> None:
        if self._shortcut is None:
            return
        try:
            self._shortcut.activated.disconnect(self._on_shortcut_activated)
        except (TypeError, RuntimeError):
            pass
        self._shortcut.setParent(None)
        self._shortcut.deleteLater()
        self._shortcut = None
