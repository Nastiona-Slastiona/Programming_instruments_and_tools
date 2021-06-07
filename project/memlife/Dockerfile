# pull official base image
FROM python:3.8.3-alpine
# set work directory
WORKDIR /usr/src/memlife
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip
# install dependencies
RUN apk update && apk add libpq
RUN pip install djangorestframework 
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk add libffi-dev libressl-dev \
    && apk add --no-cache jpeg-dev zlib-dev libjpeg \
    && apk add rust cargo 
RUN pip install cryptography
RUN pip install django-allauth
RUN pip install markdown 
RUN pip install django-filter

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps


RUN pip install PyYAML

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh .

# copy project
COPY . .

RUN chmod +x /usr/src/memlife/entrypoint.sh
ENTRYPOINT ["/usr/src/memlife/entrypoint.sh"]