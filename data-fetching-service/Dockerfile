# pull official base image
FROM python:3.11-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY ./requirements.txt /usr/src/app/

# install requirements
RUN pip install -r requirements.txt

EXPOSE 5000