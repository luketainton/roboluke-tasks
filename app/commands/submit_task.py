#!/usr/bin/env python3

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
from app.utils.n8n import submit_task, get_tasks

log: logging.Logger = logging.getLogger(__name__)


class SubmitTaskCommand(Command):
    def __init__(self) -> None:
        super().__init__(
            command_keyword="submit_feedback_dstgmyn",
            help_message="Submit Task",
            chained_commands=[SubmitTaskCallback(), MyTasksCallback()],
            delete_previous_message=True,
        )
        self.sender: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        self.sender = activity.get("actor").get("id")

    def execute(self, message, attachment_actions, activity) -> Response:
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
                                f"Add a task to {config.admin_first_name}'s To Do list. All fields are required.",
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
                            Text(id="issue_title", placeholder="Summary", maxLength=100),
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
                                    placeholder="Requester Email (leave blank to submit for yourself)",
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
                    title="My Tasks",
                    data={
                        "callback_keyword": "my_tasks_callback_rbamzfyx",
                        "sender": self.sender,
                    },
                ),
                Submit(title="Cancel", data={"command_keyword": "exit"}),
            ],
        )
        return response_from_adaptive_card(card)


class SubmitTaskCallback(Command):
    def __init__(self) -> None:
        super().__init__(
            card_callback_keyword="submit_task_callback_rbamzfyx", delete_previous_message=True
        )
        self.msg: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> None:
        issue_title: str = attachment_actions.inputs.get("issue_title")
        issue_description: str = attachment_actions.inputs.get("issue_description")
        completion_date: str = attachment_actions.inputs.get("completion_date")

        sender: str = attachment_actions.inputs.get("sender")
        issue_requester: str = attachment_actions.inputs.get("issue_requester") or sender

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
            "Submitting your task..." if result else "Failed to submit task. Please try again."
        )

    def execute(self, message, attachment_actions, activity) -> str:
        return self.msg


class MyTasksCallback(Command):
    def __init__(self) -> None:
        super().__init__(
            card_callback_keyword="my_tasks_callback_rbamzfyx", delete_previous_message=True
        )
        self.msg: str = ""

    def pre_execute(self, message, attachment_actions, activity) -> str:
        return "Getting your tasks..."

    def execute(self, message, attachment_actions, activity) -> str | None:
        sender: str = attachment_actions.inputs.get("sender")
        result: bool = get_tasks(requestor=sender)
        if not result:
            return "Failed to get tasks. Please try again."
        return
