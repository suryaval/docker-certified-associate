FROM ubuntu:latest as builder
WORKDIR /root/
EXPOSE 8080
RUN apt update -y && \
    apt install python -y
ADD something.py /root/
ENTRYPOINT python something.py
