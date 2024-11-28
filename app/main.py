"""Main module."""

import sys

from webex_bot.webex_bot import WebexBot

from app.commands.exit import ExitCommand
from app.commands.submit_task import SubmitTaskCommand
from app.utils.config import config


def create_bot() -> WebexBot:
    """Create and return a Webex Bot object."""
    webex_bot: WebexBot = WebexBot(
        bot_name=config.bot_name,
        teams_bot_token=config.webex_token,
        approved_domains=config.approved_domains,
        approved_rooms=config.approved_rooms,
        approved_users=config.approved_users,
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
        sys.exit(0)
