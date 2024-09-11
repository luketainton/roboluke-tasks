#!/usr/bin/env python3

# ruff: noqa: E402 pylint: disable=wrong-import-position

"""Provides test cases for app/utils/config.py."""

import os

vars: dict = {
    "APP_VERSION": "dev",
    "BOT_NAME": "TestBot",
    "WEBEX_API_KEY": "testing",
    "ADMIN_FIRST_NAME": "Test",
    "ADMIN_EMAIL": "test@test.com",
    "N8N_WEBHOOK_URL": "https://n8n.test.com/webhook/abcdefg",
    "SENTRY_ENABLED": "false",
    "SENTRY_DSN": "http://localhost",
    "APPROVED_USERS": "test@test.com",
    "APPROVED_DOMAINS": "test.com",
    "APPROVED_ROOMS": "test",
}


for var, value in vars.items():
    os.environ[var] = value

# needs to be imported AFTER environment variables are set
from app.utils.config import config  # pragma: no cover


def test_config() -> None:
    assert config.admin_emails == vars["ADMIN_EMAIL"].split(",")
    assert config.admin_first_name == vars["ADMIN_FIRST_NAME"]
    assert config.approved_domains == vars["APPROVED_DOMAINS"].split(",")
    assert config.approved_rooms == vars["APPROVED_ROOMS"].split(",")
    assert config.approved_users == vars["APPROVED_USERS"].split(",")
    assert config.bot_name == vars["BOT_NAME"]
    assert config.n8n_webhook_url == vars["N8N_WEBHOOK_URL"]
    assert config.sentry_enabled == bool(vars["SENTRY_ENABLED"].upper() == "TRUE")
    assert config.version == vars["APP_VERSION"]
    assert config.webex_token == vars["WEBEX_API_KEY"]

    if config.sentry_enabled:
        assert config.sentry_dsn == vars["SENTRY_DSN"]
    else:
        assert config.sentry_dsn == ""
