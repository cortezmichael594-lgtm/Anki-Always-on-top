# Copyright (C) 2026 AnkiCraft
# This file is part of Always on Top (by Ankicraft).
# License: GNU AGPL v3 <https://www.gnu.org/licenses/agpl-3.0.html>

from __future__ import annotations

import os

from aqt import mw
from aqt.qt import (
    QDesktopServices,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLabel,
    QPixmap,
    QPushButton,
    Qt,
    QTimer,
    QUrl,
    QVBoxLayout,
    QWidget,
)

from . import constants
from .settings import is_welcome_shown, mark_welcome_shown
from .strings import tr


def _open_url(url: str) -> None:
    QDesktopServices.openUrl(QUrl(url))


def _colored_button(text: str, bg: str, hover: str, tooltip: str = "") -> QPushButton:
    btn = QPushButton(text)
    btn.setStyleSheet(
        f"QPushButton {{ background-color: {bg}; color: white; border-radius: 6px;"
        f" padding: 6px 14px; border: none; }}"
        f" QPushButton:hover {{ background-color: {hover}; }}"
    )
    if tooltip:
        btn.setToolTip(tooltip)
    return btn


class WelcomeDialog(QDialog):
    def __init__(self) -> None:
        super().__init__(mw)
        self.setWindowTitle(
            tr("welcome_title", name=constants.ADDON_NAME, version=constants.ADDON_VERSION)
        )
        self.setModal(True)
        self.setMinimumWidth(460)

        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        # Logo (omitted silently if logo.png is absent)
        logo_path = os.path.join(os.path.dirname(__file__), constants.LOGO_FILENAME)
        if os.path.isfile(logo_path):
            pix = QPixmap(logo_path).scaled(
                constants.LOGO_SIZE_PX,
                constants.LOGO_SIZE_PX,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
            logo_lbl = QLabel()
            logo_lbl.setPixmap(pix)
            logo_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
            layout.addWidget(logo_lbl)

        # Title
        title_lbl = QLabel(
            tr("welcome_title", name=constants.ADDON_NAME, version=constants.ADDON_VERSION)
        )
        title_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        title_lbl.setStyleSheet(
            f"font-weight: bold; font-size: 15px; color: {constants.COLOR_ACCENT};"
        )
        layout.addWidget(title_lbl)

        # By line
        by_lbl = QLabel("by AnkiCraft")
        by_lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        by_lbl.setStyleSheet("font-size: 11px; color: gray;")
        layout.addWidget(by_lbl)

        layout.addSpacing(4)

        # Body
        body_lbl = QLabel(
            tr("welcome_body", name=constants.ADDON_NAME, version=constants.ADDON_VERSION)
        )
        body_lbl.setWordWrap(True)
        layout.addWidget(body_lbl)

        layout.addSpacing(4)

        # Support note
        note_lbl = QLabel(tr("welcome_support_note"))
        note_lbl.setWordWrap(True)
        note_lbl.setStyleSheet("font-size: 10px; color: gray;")
        layout.addWidget(note_lbl)

        layout.addSpacing(8)

        # Brand buttons row
        btn_row = QHBoxLayout()
        btn_row.setSpacing(8)

        kofi_btn = _colored_button(
            tr("kofi_button"),
            constants.COLOR_KOFI_BG,
            constants.COLOR_KOFI_HOVER,
            tr("kofi_tooltip"),
        )
        kofi_btn.clicked.connect(lambda: _open_url(constants.URL_KOFI))
        btn_row.addWidget(kofi_btn)

        patreon_btn = _colored_button(
            tr("patreon_button"),
            constants.COLOR_PATREON_BG,
            constants.COLOR_PATREON_HOVER,
        )
        patreon_btn.clicked.connect(lambda: _open_url(constants.URL_PATREON))
        btn_row.addWidget(patreon_btn)

        if constants.ANKIWEB_ID:
            rate_btn = _colored_button(
                tr("rate_button"),
                constants.COLOR_RATE_BG,
                constants.COLOR_RATE_HOVER,
            )
            rate_btn.clicked.connect(lambda: _open_url(constants.ANKIWEB_REVIEW_URL))
            btn_row.addWidget(rate_btn)

        layout.addLayout(btn_row)
        layout.addSpacing(4)

        # Close button (system style, focused, default)
        close_box = QDialogButtonBox(self)
        close_btn = close_box.addButton(
            tr("welcome_close"), QDialogButtonBox.ButtonRole.AcceptRole
        )
        if close_btn is not None:
            close_btn.setDefault(True)
            close_btn.setFocus()
        close_box.accepted.connect(self.accept)
        layout.addWidget(close_box)


def maybe_show_welcome() -> None:
    """Show WelcomeDialog once per installation, deferred by WELCOME_DELAY_MS."""
    if is_welcome_shown():
        return
    mark_welcome_shown()
    QTimer.singleShot(constants.WELCOME_DELAY_MS, _do_show_welcome)


def _do_show_welcome() -> None:
    try:
        WelcomeDialog().exec()
    except Exception as exc:
        print(f"[always_on_top] WelcomeDialog: {exc!r}")


def build_support_row(parent: QWidget) -> QHBoxLayout:
    """Sober support footer for the config dialog (no brand colours)."""
    row = QHBoxLayout()

    version_text = tr(
        "version_line", name=constants.ADDON_NAME, version=constants.ADDON_VERSION
    )
    if constants.ANKIWEB_ID:
        info_lbl = QLabel(
            f'<small>{version_text} · <a href="{constants.URL_REPORT_BUG}">'
            f'{tr("report_button")}</a></small>'
        )
    else:
        info_lbl = QLabel(f"<small>{version_text}</small>")
    info_lbl.setOpenExternalLinks(True)
    row.addWidget(info_lbl)
    row.addStretch()

    kofi_btn = QPushButton(tr("kofi_button"), parent)
    kofi_btn.setToolTip(tr("kofi_tooltip"))
    kofi_btn.clicked.connect(lambda: _open_url(constants.URL_KOFI))
    row.addWidget(kofi_btn)

    patreon_btn = QPushButton(tr("patreon_button"), parent)
    patreon_btn.clicked.connect(lambda: _open_url(constants.URL_PATREON))
    row.addWidget(patreon_btn)

    if constants.ANKIWEB_ID:
        rate_btn = QPushButton(tr("rate_button"), parent)
        rate_btn.clicked.connect(lambda: _open_url(constants.ANKIWEB_REVIEW_URL))
        row.addWidget(rate_btn)

    return row
