#!/usr/bin/env python3

# ruff: noqa: E402 pylint: disable=wrong-import-position

"""Provides test cases for app/utils/config.py."""

import os

config_vars: dict = {
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


for config_var, value in config_vars.items():
    os.environ[config_var] = value

# needs to be imported AFTER environment variables are set
from app.utils.config import config  # pragma: no cover


def test_config() -> None:
    """Test config module."""
    assert config.admin_emails == config_vars["ADMIN_EMAIL"].split(",")
    assert config.admin_first_name == config_vars["ADMIN_FIRST_NAME"]
    assert config.approved_domains == config_vars["APPROVED_DOMAINS"].split(",")
    assert config.approved_rooms == config_vars["APPROVED_ROOMS"].split(",")
    assert config.approved_users == config_vars["APPROVED_USERS"].split(",")
    assert config.bot_name == config_vars["BOT_NAME"]
    assert config.n8n_webhook_url == config_vars["N8N_WEBHOOK_URL"]
    assert config.sentry_enabled == bool(
        config_vars["SENTRY_ENABLED"].upper() == "TRUE"
    )
    assert config.version == config_vars["APP_VERSION"]
    assert config.webex_token == config_vars["WEBEX_API_KEY"]

    if config.sentry_enabled:
        assert config.sentry_dsn == config_vars["SENTRY_DSN"]
    else:
        assert config.sentry_dsn == ""
