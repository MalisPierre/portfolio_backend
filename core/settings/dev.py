from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://pierre-malis-portfolio-frontend.s3-website.eu-north-1.amazonaws.com",
]