from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True#False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = [
    "http://pierre-malis-portfolio-frontend.s3-website.eu-north-1.amazonaws.com"
]