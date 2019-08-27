FROM ubuntu:latest as builder
WORKDIR /root/
RUN apt update -y
COPY ./something.py WORKDIR

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /root/something.py WORKDIR
CMD [ "ls","-ltr" ]
