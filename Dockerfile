# syntax=docker/dockerfile:1.4
FROM python:3.13.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN --mount=type=cache,target=/var/cache/apk <<EOF
apk update
apk add git
EOF

COPY ./requirements.txt /app/requirements.txt
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY . /app
RUN apk del git

ENTRYPOINT ["hypercorn", "-b", "0.0.0.0:8000", "l4q:create_app()"]

EXPOSE 8000
