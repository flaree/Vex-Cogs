import datetime
from typing import Dict

import pytz

from .data import ZONE_KEYS


def gen_replacements() -> Dict[str, str]:
    replacements: Dict[str, str] = {}
    for key, zone in ZONE_KEYS.items():
        foramtted_time = datetime.datetime.now(pytz.timezone(zone)).strftime("%I:%M%p").lstrip("0")
        replacements[key] = foramtted_time

        formatted_24h_time = datetime.datetime.now(pytz.timezone(zone)).strftime("%H:%M")
        replacements[f"{key}-24h"] = formatted_24h_time
    return replacements
