from .base import *  # noqa: F401

SENTRY_DSN = os.getenv('SENTRY_DSN')

if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        SENTRY_DSN,
        traces_sample_rate=1.0,
        integrations=[DjangoIntegration()],
    )

DEBUG = False

INTERNAL_IPS = [
    '127.0.0.1',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {'format': '%(asctime)s %(levelname)s %(module)s: %(message)s'}
    },
    'handlers': {
        'analyzer': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/opt/python/log/analyzer.log',
            'formatter': 'verbose',
        }
    },
    'loggers': {
        'analyzer': {'handlers': ['analyzer'], 'level': 'DEBUG', 'propagate': True}
    },
}
