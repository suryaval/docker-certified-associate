FROM ubuntu:latest as builder
WORKDIR /root/
RUN apt update -y
COPY something.py /root/
ENTRYPOINT python something.py
