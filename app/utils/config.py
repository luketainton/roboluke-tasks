#!/usr/bin/env python3


import os


class Config:
    def __init__(self) -> None:
        self.__bot_name: str = os.environ["BOT_NAME"]
        self.__webex_token: str = os.environ["WEBEX_API_KEY"]
        self.__admin_first_name: str = os.environ["ADMIN_FIRST_NAME"]
        self.__admin_emails: list = os.environ["ADMIN_EMAIL"].split(",")
        self.__n8n_webhook_url: str = os.environ["N8N_WEBHOOK_URL"]

    @property
    def bot_name(self) -> str:
        return self.__bot_name

    @property
    def webex_token(self) -> str:
        return self.__webex_token

    @property
    def admin_first_name(self) -> str:
        return self.__admin_first_name

    @property
    def admin_emails(self) -> list:
        return self.__admin_emails

    @property
    def n8n_webhook_url(self) -> str:
        return self.__n8n_webhook_url


config: Config = Config()
