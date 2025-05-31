"""N8N utils module."""

import requests

from app.utils.config import config


def __n8n_post(data: dict) -> bool:
    """Post data to N8N webhook URL.

    Args:
        data (dict): Data to post to webhook URL.

    Returns:
        bool: True if successful, else False.
    """
    headers: dict = {"Content-Type": "application/json"}
    resp: requests.Response = requests.post(
        url=config.n8n_webhook_url,
        headers=headers,
        json=data,
        timeout=10,
        verify=True,
    )
    return bool(resp.status_code == 200)


def submit_task(summary, description, completion_date, requestor) -> bool:
    """Submit task to N8N webhook URL.

    Args:
        summary (str): Summary of task.
        description (str): Description of task.
        completion_date (str): Completion date of task.
        requestor (str): Requestor of task.

    Returns:
        bool: True if successful, else False.
    """
    data: dict = {
        "requestor": requestor,
        "title": summary,
        "description": description,
        "completiondate": completion_date,
    }
    _data = __n8n_post(data=data)
    return _data


def get_tasks(requestor) -> bool:
    """Get tasks from N8N webhook URL.

    Args:
        requestor (str): Requestor of tasks.

    Returns:
        bool: True if successful, else False.
    """
    headers: dict = {"Content-Type": "application/json"}
    resp: requests.Response = requests.get(
        url=config.n8n_webhook_url,
        headers=headers,
        timeout=10,
        verify=True,
        params={"requestor": requestor},
    )
    _data = bool(resp.status_code == 200)
    return _data
