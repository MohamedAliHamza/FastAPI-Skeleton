FROM python:3.11.4-slim-buster

RUN apt-get update && apt-get install -y build-essential libpq-dev

WORKDIR /usr/src/app

ARG BUILD_ENVIRONMENT=local
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements .

RUN pip install -r ${BUILD_ENVIRONMENT}.txt

COPY . .