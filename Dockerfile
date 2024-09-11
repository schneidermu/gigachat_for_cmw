FROM python:3.10

RUN apt-get update

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY /app /app

CMD uwsgi --ini /app/wsgi.ini