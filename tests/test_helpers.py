#!/usr/bin/env python3

"""Provides test cases for app/utils/helpers.py."""

from app.utils.helpers import validate_email_syntax  # pragma: no cover


def test_validate_email_syntax_true() -> None:
    email: str = "test@test.com"
    assert validate_email_syntax(email)


def test_validate_email_syntax_false1() -> None:
    email: str = "test@test"
    assert not validate_email_syntax(email)


def test_validate_email_syntax_false2() -> None:
    email: str = "test"
    assert not validate_email_syntax(email)
