#!/bin/sh
set -e

# start gunicorn in background
gunicorn workspace.wsgi:application \
  --bind 127.0.0.1:8001 \
  --workers 3 \
  --daemon

# start nginx in foreground (keeps container alive)
nginx -g "daemon off;"