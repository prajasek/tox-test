FROM python:3.12

WORKDIR /usr/home/prajasek

COPY . /usr/home/prajasek

RUN pip install -r requirements.txt

CMD ["/bin/sh"]
