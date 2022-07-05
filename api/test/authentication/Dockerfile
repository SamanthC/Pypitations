FROM debian:latest

RUN apt-get update --fix-missing && apt-get install python3-pip -y && pip3 install requests==2.27.1

ADD auth.py auth2.py

CMD python3 auth2.py
