# Copyright (C) 2026 AnkiCraft
# This file is part of Always on Top (by Ankicraft).
# License: GNU AGPL v3 <https://www.gnu.org/licenses/agpl-3.0.html>

from __future__ import annotations

from aqt import gui_hooks, mw

from . import constants
from .logic import AlwaysOnTopManager
from .support import maybe_show_welcome
from .ui import open_config_dialog

_manager = AlwaysOnTopManager()


def _open_config() -> None:
    open_config_dialog(_manager)


gui_hooks.add_cards_did_init.append(_manager.on_add_cards_init)
gui_hooks.main_window_did_init.append(maybe_show_welcome)
mw.addonManager.setConfigAction(constants.ADDON_PACKAGE, _open_config)
mw.addonManager.setConfigUpdatedAction(constants.ADDON_PACKAGE, _manager.on_config_updated)
_manager.start()
