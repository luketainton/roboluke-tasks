import sentry_sdk
from sentry_sdk.integrations.stdlib import StdlibIntegration

from app.utils.config import config


if config.sentry_enabled:
    apm = sentry_sdk.init(
        dsn=config.sentry_dsn,
        enable_tracing=True,
        environment=config.environment,
        integrations=[StdlibIntegration()],
        spotlight=True
    )
else:
    apm = None
