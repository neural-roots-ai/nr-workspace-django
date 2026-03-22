# ── Stage 1: Python/Django build ────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
WORKDIR /app/src

# collect static files into a folder
RUN python manage.py collectstatic --no-input --clear

# ── Stage 2: Final image with nginx + gunicorn ───────
FROM python:3.12-slim

# install nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# copy python deps from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# copy app source
COPY --from=builder /app/src ./src

# copy collected static files
COPY --from=builder /app/src/static_root ./src/static_root

# copy nginx config
COPY nginx.conf /etc/nginx/nginx.conf

RUN cat > /docker-entrypoint.sh << 'EOF'
#!/bin/sh
set -e

echo "Running migrations..."
cd /app/src
python manage.py migrate --no-input

echo "Starting gunicorn..."
gunicorn workspace.wsgi:application \
  --bind 127.0.0.1:8001 \
  --workers 3 \
  --daemon \
  --log-file /var/log/gunicorn.log \
  --error-logfile /var/log/gunicorn-error.log

echo "Starting nginx..."
exec nginx -g "daemon off;"
EOF

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]