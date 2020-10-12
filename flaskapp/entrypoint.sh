#!/bin/bash
ls
pwd
cd ..
exec gunicorn --log-level=debug  --preload --config /flaskapp/gunicorn_config.py "flaskapp.wsgi:app" -b 0.0.0.0:$PORT
