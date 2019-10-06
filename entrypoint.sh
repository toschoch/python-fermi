#!/bin/sh

python manage.py db upgrade
python manage.py run -h 0.0.0.0 -p 80
