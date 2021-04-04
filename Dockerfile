FROM python:3.9-alpine
MAINTAINER 4mr0m3r0

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

WORKDIR /app
COPY . /app

RUN adduser -D user
USER user