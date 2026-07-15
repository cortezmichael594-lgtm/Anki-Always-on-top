# Copyright (C) 2026 AnkiCraft
# This file is part of Always on Top (by Ankicraft).
# License: GNU AGPL v3 <https://www.gnu.org/licenses/agpl-3.0.html>

from __future__ import annotations

ADDON_PACKAGE: str = __name__.split(".")[0]
ADDON_NAME: str = "Always on Top"
ADDON_DISPLAY_NAME: str = "Always on Top (by Ankicraft)"
ADDON_VERSION: str = "1.0.0"
AUTHOR_NAME: str = "AnkiCraft"

ANKIWEB_ID: str = "894169326"
ANKIWEB_PAGE_URL: str = f"https://ankiweb.net/shared/info/{ANKIWEB_ID}"
ANKIWEB_REVIEW_URL: str = f"https://ankiweb.net/shared/review/{ANKIWEB_ID}"
URL_KOFI: str = "https://ko-fi.com/ankicraft"
URL_PATREON: str = "https://www.patreon.com/cw/Ankicraft594"
URL_REPORT_BUG: str = ANKIWEB_PAGE_URL

LOGO_FILENAME: str = "logo.png"
LOGO_SIZE_PX: int = 72

COLOR_ACCENT: str = "#7C5CE0"
COLOR_KOFI_BG: str = "#29ABE0"
COLOR_KOFI_HOVER: str = "#1E8FBF"
COLOR_PATREON_BG: str = "#FF424D"
COLOR_PATREON_HOVER: str = "#E0313C"
COLOR_RATE_BG: str = "#F5A623"
COLOR_RATE_HOVER: str = "#D98E12"

CONFIG_KEY_META: str = "_meta"
META_KEY_WELCOME_SHOWN: str = "welcome_shown"
WELCOME_DELAY_MS: int = 2000

DEFAULT_SHORTCUT: str = "Ctrl+Shift+T"
CONFIG_KEY_SHORTCUT: str = "shortcut"
TOOLTIP_PERIOD_MS: int = 1500
