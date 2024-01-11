FROM python:slim-bullseye

COPY ./hello.py /opt/python/

WORKDIR /opt/python

ENTRYPOINT ["python", "hello.py"]