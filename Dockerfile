# pull official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# install dependencies
RUN apk update \
    && apk add git \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements/development.txt \
    && python -m compileall . \
    && apk del git \
    && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app

# develop like environment
CMD ["python", "main.py"]