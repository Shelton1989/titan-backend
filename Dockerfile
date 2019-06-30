FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /site_manager

WORKDIR /site_manager

ADD . /site_manager

RUN pip install -r requirements.txt