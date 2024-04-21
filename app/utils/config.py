"""Configuration module."""

import os


class Config:
    """Configuration module."""
    def __init__(self) -> None:
        """Configuration module."""
        self.__environment: str = os.environ.get("APP_LIFECYCLE", "DEV").upper()
        self.__bot_name: str = os.environ["BOT_NAME"]
        self.__webex_token: str = os.environ["WEBEX_API_KEY"]
        self.__admin_first_name: str = os.environ["ADMIN_FIRST_NAME"]
        self.__admin_emails: list = os.environ["ADMIN_EMAIL"].split(",")
        self.__n8n_webhook_url: str = os.environ["N8N_WEBHOOK_URL"]
        self.__sentry_dsn: str = os.environ.get("SENTRY_DSN", "")
        self.__sentry_enabled: bool = bool(
            os.environ.get("SENTRY_ENABLED", "False").upper() == "TRUE"
            and self.__sentry_dsn != ""
        )

    @property
    def environment(self) -> str:
        """Returns the current app lifecycle."""
        return self.__environment

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
        return self.__bot_name

    @property
    def webex_token(self) -> str:
        """Returns the Webex API key."""
        return self.__webex_token

    @property
    def admin_first_name(self) -> str:
        """Returns the first name of the bot admin."""
        return self.__admin_first_name

    @property
    def admin_emails(self) -> list:
        """Returns a list of admin email addresses."""
        return self.__admin_emails

    @property
    def n8n_webhook_url(self) -> str:
        """Returns the n8n webhook URL."""
        return self.__n8n_webhook_url


config: Config = Config()
