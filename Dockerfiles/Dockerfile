FROM ubuntu:latest as builder
WORKDIR /root/
RUN apt update -y
CMD [ "ls","-ltr","&&","touch","something.py" ]

FROM alpine:latest
WORKDIR /root/
COPY --from=builder /root/something.py WORKDIR
CMD [ "ls","-ltr" ]
