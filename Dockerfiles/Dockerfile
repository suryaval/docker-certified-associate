FROM ubuntu:latest as builder
WORKDIR /root/
EXPOSE 8080
RUN apt update -y && \
    apt install python3 -y
ADD something.py /root/
ENTRYPOINT python3 something.py
