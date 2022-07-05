FROM debian:latest

RUN mkdir /app

WORKDIR /app

COPY /api/requirements.txt /api/main.py /models data/mitbih_test.csv ./

RUN apt-get update --fix-missing && apt-get install python3-pip -y && pip3 install -r requirements.txt

CMD uvicorn main:api --host 0.0.0.0