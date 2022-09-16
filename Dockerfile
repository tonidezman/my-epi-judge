FROM python:3.10.6-bullseye

RUN pip install ipython

COPY . .
