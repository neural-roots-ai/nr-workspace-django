# Use the official Python image from Docker Hub
FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

WORKDIR /app/src

RUN python manage.py collectstatic --no-input --clear