# ── Stage 1: Python/Django build ────────────────────
FROM python:3.12-slim AS builder

WORKDIR /app
COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
WORKDIR /app/src

# collect static files into a folder
RUN python manage.py collectstatic --no-input --clear
# ── Stage 2: Final image ─────────────────────────────
FROM python:3.12-slim

RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn
COPY --from=builder /app/src ./src
COPY --from=builder /app/src/static_root ./src/static_root

COPY nginx.conf /etc/nginx/nginx.conf

# ✅ no external file needed — written directly into image
RUN echo '#!/bin/sh' > /docker-entrypoint.sh && \
    echo 'set -e' >> /docker-entrypoint.sh && \
    echo 'cd /app/src' >> /docker-entrypoint.sh && \
    echo 'echo "Running migrations..."' >> /docker-entrypoint.sh && \
    echo 'python manage.py migrate --no-input' >> /docker-entrypoint.sh && \
    echo 'echo "Starting gunicorn..."' >> /docker-entrypoint.sh && \
    echo 'gunicorn workspace.wsgi:application --bind 127.0.0.1:8001 --workers 3 --daemon --log-file /var/log/gunicorn.log --error-logfile /var/log/gunicorn-error.log' >> /docker-entrypoint.sh && \
    echo 'echo "Starting nginx..."' >> /docker-entrypoint.sh && \
    echo 'exec nginx -g "daemon off;"' >> /docker-entrypoint.sh && \
    chmod +x /docker-entrypoint.sh

EXPOSE 80

ENTRYPOINT ["/docker-entrypoint.sh"]