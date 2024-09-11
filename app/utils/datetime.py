#!/usr/bin/env python3

from datetime import datetime
from zoneinfo import ZoneInfo


def timestamp_to_date(timestamp: int) -> str:
    """Convert timestamp to date.

    Args:
        timestamp (int): Timestamp to convert.

    Returns:
        str: Date in the format YYYY-MM-DD.
    """
    return datetime.fromtimestamp(timestamp=timestamp, tz=ZoneInfo("UTC")).strftime(
        "%Y-%m-%d"
    )
