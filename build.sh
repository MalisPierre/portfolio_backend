#!/usr/bin/env bash

set -o errexit  # exit on error

pip install -r core/requirements/common.txt
pip install -r core/requirements/production.txt

python manage.py collectstatic --no-input
python manage.py migrate
