from .base import * 

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "https://b071-41-80-112-187.ngrok-free.app", "https://734d-41-80-112-187.ngrok-free.app"
]


ALLOWED_HOSTS = ["*"]
CORS_ALLOW_CREDENTIALS = False



CORS_ORIGIN_WHITELIST = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "https://b071-41-80-112-187.ngrok-free.app",
    "https://734d-41-80-112-187.ngrok-free.app"

]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'http://127.0.0.1:3000'
    "https://b071-41-80-112-187.ngrok-free.app",
    "https://734d-41-80-112-187.ngrok-free.app"
    ]