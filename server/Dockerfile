FROM python:3.9

WORKDIR /server

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install project dependencies
COPY requirements.txt .
ENV VIRTUAL_ENV=/dock-venv

RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
RUN ${VIRTUAL_ENV}/bin/pip install -r requirements.txt
ENV FLASK_APP=fridge_and_larder.py