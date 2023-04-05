# RoboLuke - Tasks

## Description
Add tasks to a Wekan to do list via Webex and n8n.

## How to install
1. Clone the repository
2. Copy `.env.default` to `.env`
3. Edit `.env` as required:
    - `ADMIN_EMAIL` - comma-separated list of admin (who owns the to-do list) email addresses
    - `ADMIN_FIRST_NAME` - admin first name
    - `BOT_NAME` - Webex bot name
    - `N8N_WEBHOOK_URL` - n8n webhook URL
    - `WEBEX_API_KEY` - Webex API key

## How to use
1. Install Docker and Docker Compose
2. Run `docker-compose up -d`
