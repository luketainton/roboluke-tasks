export $(cat .env.test | xargs)
python -B -m app.main
unset ADMIN_EMAIL ADMIN_FIRST_NAME APP_LIFECYCLE APP_VERSION APPROVED_DOMAINS APPROVED_ROOMS APPROVED_USERS BOT_NAME N8N_WEBHOOK_URL WEBEX_API_KEY
