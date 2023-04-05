#!/usr/bin/env python3

import logging

from webex_bot.models.command import Command

log: logging.Logger = logging.getLogger(__name__)


class ExitCommand(Command):
    def __init__(self) -> None:
        super().__init__(
            command_keyword="exit",
            help_message="Exit",
            delete_previous_message=True,
        )
        self.sender: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        pass

    def execute(self, message, attachment_actions, activity) -> None:
        pass

    def post_execute(self, message, attachment_actions, activity) -> None:
        pass
