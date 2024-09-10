FROM python:3.10.6-alpine3.16

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

WORKDIR /app

