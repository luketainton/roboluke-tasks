"""Exit command."""

import logging

from webex_bot.models.command import Command

log: logging.Logger = logging.getLogger(__name__)


class ExitCommand(Command):
    """Exit command class."""

    def __init__(self) -> None:
        """Exit command class."""
        super().__init__(
            command_keyword="exit",
            help_message="Exit",
            delete_previous_message=True,
        )
        self.sender: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        """Pre-execute method."""

    def execute(self, message, attachment_actions, activity) -> None:
        """Execute method."""

    def post_execute(self, message, attachment_actions, activity) -> None:
        """Post-execute method."""
