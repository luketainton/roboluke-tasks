import requests

from app.utils.config import config


def __n8n_post(data: dict) -> bool:
    headers: dict = {"Content-Type": "application/json"}
    resp: requests.Response = requests.post(
        url=config.n8n_webhook_url,
        headers=headers,
        json=data,
        timeout=10,
        verify=False,
    )
    return bool(resp.status_code == 200)


def submit_task(summary, description, completion_date, requestor) -> bool:
    data: dict = {
        "requestor": requestor,
        "title": summary,
        "description": description,
        "completiondate": completion_date,
    }
    return __n8n_post(data=data)


def get_tasks(requestor) -> bool:
    headers: dict = {"Content-Type": "application/json"}
    resp: requests.Response = requests.get(
        url=config.n8n_webhook_url,
        headers=headers,
        timeout=10,
        verify=False,
        params={"requestor": requestor},
    )
    return bool(resp.status_code == 200)
