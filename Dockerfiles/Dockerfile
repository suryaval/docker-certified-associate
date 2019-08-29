FROM ubuntu:latest as builder
WORKDIR /root/
RUN apt update -y
ADD something.py /root/
ENTRYPOINT python something.py
