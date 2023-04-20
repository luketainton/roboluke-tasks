export $(cat .env | xargs)
python -B -m app.main
unset BOT_NAME WEBEX_API_KEY ADMIN_FIRST_NAME ADMIN_EMAIL N8N_WEBHOOK_URL