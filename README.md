# RoboLuke - Tasks

## Description
Add tasks to a Wekan to do list via Webex and n8n.

## How to install
1. Clone the repository
2. Copy `.env.default` to `.env`
3. Edit `.env` as required:
    - `ADMIN_EMAIL` - comma-separated list of admin (who owns the to-do list) email addresses
    - `ADMIN_FIRST_NAME` - admin first name
    - `APP_LIFECYCLE` - for use in Sentry only, set the name of the environment
    - `APPROVED_DOMAINS` - comma-separated list of domains that users are allowed to message the bot from
    - `APPROVED_ROOMS` - comma-separated list of room IDs that users are allowed to message the bot from
    - `APPROVED_USERS` - comma-separated list of email addresses of approved users
    - `BOT_NAME` - Webex bot name
    - `N8N_WEBHOOK_URL` - n8n webhook URL
    - `SENTRY_DSN` - for use in Sentry only, set the DSN of the Sentry project
    - `SENTRY_ENABLED` - for use in Sentry only, enable sending data to Sentry
    - `WEBEX_API_KEY` - Webex API key

## How to use
1. Install Docker and Docker Compose
2. Run `docker-compose up -d`
