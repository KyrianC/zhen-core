FROM python:3.9.7-alpine
    MAINTAINER Kyrian Castel <ckyrian@protonmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app

RUN apk update \
    # needed on Alpine for the cryptography and psycopg2 packages
    && apk add gcc postgresql-dev musl-dev python3-dev libffi-dev openssl-dev cargo

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8888

COPY . .
