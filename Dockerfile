FROM python:alpine3.13

WORKDIR /project0/

ADD . .

CMD python3 main.py
