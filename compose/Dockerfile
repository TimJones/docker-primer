FROM python:2.7

MAINTAINER Tim Jones <tim@spotahome.com>

EXPOSE 5000

ADD . /code

WORKDIR /code

RUN pip install -r requirements.txt

CMD python app.py
