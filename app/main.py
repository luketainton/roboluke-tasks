#!/usr/bin/env python3

import sentry_sdk
from sentry_sdk.integrations.stdlib import StdlibIntegration

from webex_bot.webex_bot import WebexBot

from app.commands.exit import ExitCommand
from app.commands.submit_task import SubmitTaskCommand
from app.utils.config import config


if config.sentry_enabled:
    apm = sentry_sdk.init(
        dsn=config.sentry_dsn,
        enable_tracing=True,
        environment=config.environment,
        integrations=[StdlibIntegration()],
        spotlight=True
    )


def create_bot() -> WebexBot:
    # Create a Bot Object
    webex_bot: WebexBot = WebexBot(
        bot_name=config.bot_name,
        teams_bot_token=config.webex_token,
        approved_domains=["cisco.com"],
    )
    webex_bot.commands.clear()
    webex_bot.add_command(SubmitTaskCommand())
    webex_bot.add_command(ExitCommand())
    webex_bot.help_command = SubmitTaskCommand()
    webex_bot.help_command.delete_previous_message = True

    return webex_bot


if __name__ == "__main__":
    try:
        bot: WebexBot = create_bot()
        bot.run()
    except KeyboardInterrupt:
        print("Shutting down bot...")
        exit()
