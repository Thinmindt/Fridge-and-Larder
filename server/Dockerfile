From python:3.9

WORKDIR /server

# Install project dependencies
COPY requirements.txt .
ENV VIRTUAL_ENV=/dock-venv
RUN python -m venv ${VIRTUAL_ENV}
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
RUN ${VIRTUAL_ENV}/bin/pip install -r requirements.txt
ENV FLASK_APP=fridge_and_larder.py

CMD [ "flask", "run",  "-p", "5001", "-h", "0.0.0.0" ]