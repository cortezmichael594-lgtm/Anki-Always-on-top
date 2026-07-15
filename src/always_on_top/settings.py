# Copyright (C) 2026 AnkiCraft
# This file is part of Always on Top (by Ankicraft).
# License: GNU AGPL v3 <https://www.gnu.org/licenses/agpl-3.0.html>

from __future__ import annotations

from dataclasses import dataclass

from aqt import mw
from aqt.qt import QKeySequence

from . import constants


@dataclass(frozen=True)
class Settings:
    shortcut: str


def _sanitize_shortcut(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        return constants.DEFAULT_SHORTCUT
    text = value.strip()
    if QKeySequence(text).isEmpty():
        return constants.DEFAULT_SHORTCUT
    return text


def load_settings() -> Settings:
    raw = mw.addonManager.getConfig(constants.ADDON_PACKAGE)
    data: dict[str, object] = raw if isinstance(raw, dict) else {}
    return Settings(shortcut=_sanitize_shortcut(data.get(constants.CONFIG_KEY_SHORTCUT)))


def save_settings(settings: Settings) -> None:
    # Read existing config first so _meta and other keys are preserved.
    raw = mw.addonManager.getConfig(constants.ADDON_PACKAGE)
    data: dict = raw if isinstance(raw, dict) else {}
    data[constants.CONFIG_KEY_SHORTCUT] = settings.shortcut
    mw.addonManager.writeConfig(constants.ADDON_PACKAGE, data)


def is_welcome_shown() -> bool:
    raw = mw.addonManager.getConfig(constants.ADDON_PACKAGE)
    data: dict = raw if isinstance(raw, dict) else {}
    meta = data.get(constants.CONFIG_KEY_META, {})
    if not isinstance(meta, dict):
        return False
    return bool(meta.get(constants.META_KEY_WELCOME_SHOWN, False))


def mark_welcome_shown() -> None:
    raw = mw.addonManager.getConfig(constants.ADDON_PACKAGE)
    data: dict = raw if isinstance(raw, dict) else {}
    if not isinstance(data.get(constants.CONFIG_KEY_META), dict):
        data[constants.CONFIG_KEY_META] = {}
    data[constants.CONFIG_KEY_META][constants.META_KEY_WELCOME_SHOWN] = True
    mw.addonManager.writeConfig(constants.ADDON_PACKAGE, data)
