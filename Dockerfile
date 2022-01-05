FROM python:3.9.9-slim

WORKDIR /work

ADD samplelib samplelib
ADD tests tests
ADD requirements.txt requirements.txt
ADD setup.py setup.py
ADD MANIFEST.in MANIFEST.in

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install pytest

CMD bash