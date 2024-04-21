#!/usr/bin/env python3

import pytz

from datetime import datetime


def timestamp_to_date(timestamp: int) -> str:
    """Convert timestamp to date.
    
    Args:
        timestamp (int): Timestamp to convert.
    
    Returns:
        str: Date in the format YYYY-MM-DD.
    """
    return datetime.fromtimestamp(timestamp=timestamp, tz=pytz.utc).strftime("%Y-%m-%d")

