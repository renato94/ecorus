#!/bin/bash
exec gunicorn --log-level debug  --preload --config /flaskapp/gunicorn_config.py  wsgi:app -b 0.0.0.0:$PORT
