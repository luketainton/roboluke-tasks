#!/usr/bin/env python3

"""Provides test cases for app/utils/datetime.py."""

import pytest

from app.utils.datetime import timestamp_to_date  # pragma: no cover


def test_correct() -> None:
    timestamp: int = 1680722218
    result: str = timestamp_to_date(timestamp)
    assert result == "2023-04-05"


def test_invalid() -> None:
    timestamp: str = "hello"
    with pytest.raises(TypeError) as excinfo:
        timestamp_to_date(timestamp)
    assert "'str' object cannot be interpreted as an integer" in str(excinfo.value)
