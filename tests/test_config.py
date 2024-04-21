#!/usr/bin/env python3

"""Provides test cases for app/utils/config.py."""

import os


vars: dict = {
    "BOT_NAME": "TestBot",
    "WEBEX_API_KEY": "testing",
    "ADMIN_FIRST_NAME": "Test",
    "ADMIN_EMAIL": "test@test.com",
    "N8N_WEBHOOK_URL": "https://n8n.test.com/webhook/abcdefg",
    "SENTRY_ENABLED": "false",
    "SENTRY_DSN": "http://localhost"
}


for var, value in vars.items():
    os.environ[var] = value

# needs to be imported AFTER environment variables are set
from app.utils.config import config  # pragma: no cover


def test_config() -> None:
    assert config.bot_name == vars["BOT_NAME"]
    assert config.webex_token == vars["WEBEX_API_KEY"]
    assert config.admin_first_name == vars["ADMIN_FIRST_NAME"]
    assert config.admin_emails == vars["ADMIN_EMAIL"].split(",")
    assert config.n8n_webhook_url == vars["N8N_WEBHOOK_URL"]
