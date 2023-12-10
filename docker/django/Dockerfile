FROM python:3.11

ENV PYTHONPATH "/app"
ENV PATH="${PATH}:/root/.poetry/bin"
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN apt update \
    && pip install poetry

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install

RUN mkdir ./src && touch ./src/a.py \
    && apt-get install -y python3-gdal jq

COPY ./docker/django/start.sh /start.sh
RUN chmod +x /start.sh
COPY .. /app/src