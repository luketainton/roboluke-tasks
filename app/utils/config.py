"""Configuration module."""

import os

from app.utils.helpers import validate_email_syntax


class Config:
    """Configuration module."""

    def __init__(self) -> None:
        """Configuration module."""

    @property
    def environment(self) -> str:
        """Returns the current app lifecycle."""
        return os.environ.get("APP_LIFECYCLE", "DEV").upper()

    @property
    def version(self) -> str:
        """Returns the current app version."""
        return os.environ["APP_VERSION"]

    @property
    def bot_name(self) -> str:
        """Returns the bot name."""
        return os.environ["BOT_NAME"]

    @property
    def webex_token(self) -> str:
        """Returns the Webex API key."""
        return os.environ["WEBEX_API_KEY"]

    @property
    def admin_first_name(self) -> str:
        """Returns the first name of the bot admin."""
        return os.environ["ADMIN_FIRST_NAME"]

    @property
    def admin_emails(self) -> list:
        """Returns a list of admin email addresses."""
        return os.environ["ADMIN_EMAIL"].split(",")

    @property
    def n8n_get_webhook_url(self) -> str:
        """Returns the n8n GET webhook URL."""
        return os.environ["N8N_GET_WEBHOOK_URL"]

    @property
    def n8n_post_webhook_url(self) -> str:
        """Returns the n8n POST webhook URL."""
        return os.environ["N8N_POST_WEBHOOK_URL"]

    @property
    def approved_users(self) -> list:
        """Returns a list of approved users."""
        _emails: list[str] = os.environ.get("APPROVED_USERS", "").split(",")
        _emails: list[str] = [i.strip() for i in _emails if i]
        if not _emails:
            return []
        emails = [i for i in _emails if validate_email_syntax(i)]
        return emails

    @property
    def approved_rooms(self) -> list:
        """Returns a list of approved rooms."""
        _rooms: list[str] = os.environ.get("APPROVED_ROOMS", "").split(",")
        rooms: list[str] = [i.strip() for i in _rooms if i]
        return rooms

    @property
    def approved_domains(self) -> list:
        """Returns a list of approved domains."""
        _domains: list[str] = os.environ.get("APPROVED_DOMAINS", "").split(",")
        domains: list[str] = [i.strip() for i in _domains if i]
        return domains


config: Config = Config()
