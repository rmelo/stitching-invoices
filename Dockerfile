FROM python:2
MAINTAINER rmelo <rdg.melo@gmail.com>

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . /opt/stitching-invoices
WORKDIR /opt/stitching-invoices
