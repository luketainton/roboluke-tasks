#!/usr/bin/env python3

from datetime import datetime


def timestamp_to_date(timestamp: int) -> str:
    return datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
