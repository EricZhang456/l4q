# syntax=docker/dockerfile:1.4
FROM python:3.13.7-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN <<EOF
apk update
apk add git
EOF

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . /app

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "l4q:create_app()"]
CMD ["-w 4"]

EXPOSE 8000
