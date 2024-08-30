"""Configuration module."""

import os

from app.utils.helpers import validate_email_syntax


class Config:
    """Configuration module."""

    def __init__(self) -> None:
        """Configuration module."""

        # Sentry config needs to be processed first for loop prevention.

        self.__sentry_dsn: str = os.environ.get("SENTRY_DSN", "")

        self.__sentry_enabled: bool = bool(
            os.environ.get("SENTRY_ENABLED", "False").upper() == "TRUE"
            and self.__sentry_dsn != ""
        )

    @property
    def environment(self) -> str:
        """Returns the current app lifecycle."""
        return os.environ.get("APP_LIFECYCLE", "DEV").upper()

    @property
    def version(self) -> str:
        """Returns the current app version."""
        return os.environ["APP_VERSION"]

    @property
    def sentry_enabled(self) -> bool:
        """Returns True if Sentry SDK is enabled, else False."""
        return self.__sentry_enabled

    @property
    def sentry_dsn(self) -> str:
        """Returns the Sentry DSN value if Sentry SDK is enabled AND
        Sentry DSN is set, else blank string."""
        if not self.__sentry_enabled:
            return ""
        return self.__sentry_dsn

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
    def n8n_webhook_url(self) -> str:
        """Returns the n8n webhook URL."""
        return os.environ["N8N_WEBHOOK_URL"]

    @property
    def approved_users(self) -> list:
        """Returns a list of approved users."""
        emails: list[str] = os.environ.get("APPROVED_USERS", "").split(",")
        emails = [i.strip() for i in emails if validate_email_syntax(i.strip())]
        return emails

    @property
    def approved_rooms(self) -> list:
        """Returns a list of approved rooms."""
        rooms: list[str] = os.environ.get("APPROVED_ROOMS", "").split(",")
        return [i.strip() for i in rooms]

    @property
    def approved_domains(self) -> list:
        """Returns a list of approved domains."""
        domains: list[str] = os.environ.get("APPROVED_DOMAINS", "").split(",")
        return [i.strip() for i in domains]


config: Config = Config()
