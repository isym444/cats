FROM python:3.10-slim-bullseye
WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# install system dependencies
RUN apt-get update

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py collectstatic --noinput

ENTRYPOINT [ "gunicorn", "CatProject.wsgi", "-b", "0.0.0.0:8000"]