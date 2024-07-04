# syntax=docker/dockerfile:1

FROM python:3.13.0b2-slim

WORKDIR /app

EXPOSE 8080

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 -m spacy download de_core_news_sm
RUN python3 install.py

CMD [ "python3", "webserver.py"]
