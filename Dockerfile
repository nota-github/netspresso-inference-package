FROM python:3.11

COPY . /app
WORKDIR /app

RUN apt-get update && python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache -r /app/requirements.txt

ENV HOME=/app