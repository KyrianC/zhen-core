FROM python:3.9.7-alpine
    MAINTAINER Kyrian Castel <ckyrian@protonmail.com>

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /zhen-api

RUN apk update \
    # needed on Alpine for the cryptography and psycopg2 packages
    && apk add gcc postgresql-dev musl-dev python3-dev libffi-dev openssl-dev cargo

RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN python -m pipenv install --dev --system --deploy --ignore-pipfile

EXPOSE 8000

COPY . ./
