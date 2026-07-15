# Copyright (C) 2026 AnkiCraft
# This file is part of Always on Top (by Ankicraft).
# License: GNU AGPL v3 <https://www.gnu.org/licenses/agpl-3.0.html>

from __future__ import annotations

from aqt import mw
from aqt.qt import (
    QDialog,
    QDialogButtonBox,
    QFrame,
    QHBoxLayout,
    QKeySequence,
    QKeySequenceEdit,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from . import constants
from .logic import AlwaysOnTopManager
from .settings import Settings, load_settings, save_settings
from .strings import tr
from .support import build_support_row


class _ShortcutRow:
    def __init__(self, sequence: str) -> None:
        self.label = QLabel(tr("shortcut_prefix"))
        self.edit = QKeySequenceEdit(QKeySequence(sequence))
        self.edit.setMaximumSequenceLength(1)
        self.edit.setClearButtonEnabled(True)
        # QKeySequenceEdit no expone placeholder: se aplica a su QLineEdit interno.
        line_edit = self.edit.findChild(QLineEdit)
        if line_edit is not None:
            line_edit.setPlaceholderText(tr("placeholder"))
        self.label.setBuddy(self.edit)

    def apply(self, sequence: str) -> None:
        self.edit.setKeySequence(QKeySequence(sequence))

    def sequence_text(self) -> str:
        return self.edit.keySequence().toString(QKeySequence.SequenceFormat.PortableText)


class ConfigDialog(QDialog):
    def __init__(self, manager: AlwaysOnTopManager) -> None:
        super().__init__(mw)
        self._manager = manager
        self.setWindowTitle(constants.ADDON_DISPLAY_NAME)
        self.setModal(True)

        self._row = _ShortcutRow(load_settings().shortcut)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel,
            self,
        )
        ok_button = buttons.button(QDialogButtonBox.StandardButton.Ok)
        cancel_button = buttons.button(QDialogButtonBox.StandardButton.Cancel)
        if ok_button is not None:
            ok_button.setText(tr("save"))
        if cancel_button is not None:
            cancel_button.setText(tr("cancel"))
        restore_button = QPushButton(tr("defaults"), self)
        restore_button.setAutoDefault(False)
        restore_button.clicked.connect(self._on_restore_defaults)
        buttons.addButton(restore_button, QDialogButtonBox.ButtonRole.ResetRole)
        buttons.accepted.connect(self._on_accept)
        buttons.rejected.connect(self.reject)

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(tr("shortcut_label"), self))
        shortcut_line = QHBoxLayout()
        shortcut_line.addWidget(self._row.label)
        shortcut_line.addWidget(self._row.edit, stretch=1)
        layout.addLayout(shortcut_line)
        layout.addSpacing(6)
        layout.addWidget(buttons)

        # Support footer
        sep = QFrame(self)
        sep.setFrameShape(QFrame.Shape.HLine)
        sep.setFrameShadow(QFrame.Shadow.Sunken)
        layout.addWidget(sep)
        layout.addLayout(build_support_row(self))

        self.setMinimumWidth(480)
        self._row.edit.setFocus()

    def _on_restore_defaults(self) -> None:
        self._row.apply(constants.DEFAULT_SHORTCUT)

    def _on_accept(self) -> None:
        try:
            shortcut = self._row.sequence_text().strip() or constants.DEFAULT_SHORTCUT
            save_settings(Settings(shortcut=shortcut))
            self._manager.apply_shortcut(shortcut, notify=True)
        except Exception as exc:
            print(f"[always_on_top] ConfigDialog accept: {exc!r}")
        self.accept()


def open_config_dialog(manager: AlwaysOnTopManager) -> None:
    try:
        ConfigDialog(manager).exec()
    except Exception as exc:
        print(f"[always_on_top] open_config_dialog: {exc!r}")
