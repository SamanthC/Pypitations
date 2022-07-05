FROM debian:latest

RUN apt-get update --fix-missing && apt-get install python3-pip -y && pip3 install requests==2.27.1

ADD ecg_index.py ecg_index.py

CMD python3 ecg_index.py