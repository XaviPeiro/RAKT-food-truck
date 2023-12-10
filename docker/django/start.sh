#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

python manage.py migrate
python manage.py load_food_trucks_from_csv
python manage.py runserver 0.0.0.0:8000
