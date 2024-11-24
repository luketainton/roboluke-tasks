"""Submit task command."""

import logging

from webex_bot.models.command import Command
from webex_bot.models.response import Response, response_from_adaptive_card
from webexteamssdk.models.cards import (
    AdaptiveCard,
    Column,
    ColumnSet,
    Date,
    FontSize,
    FontWeight,
    Text,
    TextBlock,
)
from webexteamssdk.models.cards.actions import Submit

from app.utils.config import config
from app.utils.n8n import get_tasks, submit_task

log: logging.Logger = logging.getLogger(__name__)


class SubmitTaskCommand(Command):
    """Submit task command."""

    def __init__(self) -> None:
        """Submit task command."""
        super().__init__(
            command_keyword="submit_feedback_dstgmyn",
            help_message="Submit Task",
            chained_commands=[SubmitTaskCallback(), MyTasksCallback()],
            delete_previous_message=True,
        )
        self.sender: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        """Pre-execute method."""
        self.sender = activity.get("actor").get("id")

    def execute(self, message, attachment_actions, activity) -> Response:
        """Execute method."""
        card_body: list = [
            ColumnSet(
                columns=[
                    Column(
                        items=[
                            TextBlock(
                                "Submit Task",
                                weight=FontWeight.BOLDER,
                                size=FontSize.MEDIUM,
                            ),
                            TextBlock(
                                f"Add a task to {config.admin_first_name}'s To Do list. "
                                + "All fields are required. Please don't use special characters.",
                                wrap=True,
                                isSubtle=True,
                            ),
                        ],
                        width=2,
                    )
                ]
            ),
            ColumnSet(
                columns=[
                    Column(
                        width=2,
                        items=[
                            Text(
                                id="issue_title", placeholder="Summary", maxLength=100
                            ),
                            Text(
                                id="issue_description",
                                placeholder="Description",
                                maxLength=1000,
                                isMultiline=True,
                            ),
                            Date(id="completion_date", placeholder="Completion Date"),
                        ],
                    ),
                ]
            ),
        ]

        if self.sender in config.admin_emails:
            card_body.append(
                ColumnSet(
                    columns=[
                        Column(
                            width=1,
                            items=[
                                Text(
                                    id="issue_requester",
                                    placeholder="Requester Email "
                                    + "(leave blank to submit for yourself)",
                                    maxLength=100,
                                ),
                            ],
                        ),
                    ]
                ),
            )

        card: AdaptiveCard = AdaptiveCard(
            body=card_body,
            actions=[
                Submit(
                    title="Submit",
                    data={
                        "callback_keyword": "submit_task_callback_rbamzfyx",
                        "sender": self.sender,
                    },
                ),
                Submit(
                    title="My Submitted Tasks",
                    data={
                        "callback_keyword": "my_tasks_callback_rbamzfyx",
                        "sender": self.sender,
                    },
                ),
                Submit(title="Cancel", data={"command_keyword": "exit"}),
            ],
        )
        _result = response_from_adaptive_card(card)
        return _result


class SubmitTaskCallback(Command):
    """Submit task callback."""

    def __init__(self) -> None:
        """Submit task callback."""
        super().__init__(
            card_callback_keyword="submit_task_callback_rbamzfyx",
            delete_previous_message=True,
        )
        self.msg: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        """Pre-execute method."""
        issue_title: str = attachment_actions.inputs.get("issue_title")
        issue_description: str = attachment_actions.inputs.get("issue_description")
        completion_date: str = attachment_actions.inputs.get("completion_date")

        sender: str = attachment_actions.inputs.get("sender")
        issue_requester: str = (
            attachment_actions.inputs.get("issue_requester") or sender
        )

        if not issue_title or not issue_description or not completion_date:
            self.msg = "Please complete all fields."
            return

        result: bool = submit_task(
            requestor=issue_requester,
            summary=issue_title,
            description=issue_description,
            completion_date=completion_date,
        )

        self.msg = (
            "Submitting your task..."
            if result
            else "Failed to submit task. Please try again."
        )

    def execute(self, message, attachment_actions, activity) -> str:
        """Execute method."""
        return self.msg


class MyTasksCallback(Command):
    """My tasks callback."""

    def __init__(self) -> None:
        """My tasks callback."""
        super().__init__(
            card_callback_keyword="my_tasks_callback_rbamzfyx",
            delete_previous_message=True,
        )
        self.msg: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> str:
        """Pre-execute method."""
        _msg: str = "Getting your tasks..."
        return _msg

    def execute(self, message, attachment_actions, activity) -> str | None:
        """Execute method."""
        sender: str = attachment_actions.inputs.get("sender")
        result: bool = get_tasks(requestor=sender)
        _msg: str = "Failed to get tasks. Please try again."
        if not result:
            return _msg
        return None
