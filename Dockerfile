FROM python:3.11

RUN mkdir -p /opt/ncservices

RUN pip install --upgrade pip

ADD requirements.txt /opt/ncservices/requirements.txt
RUN pip install --no-cache-dir -r /opt/ncservices/requirements.txt


WORKDIR /opt/ncservices
