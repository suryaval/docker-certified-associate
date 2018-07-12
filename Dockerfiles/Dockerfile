FROM ubuntu:latest as builder
WORKDIR /root/
RUN apt update -y
CMD [ "ls","-ltr","&&","touch","something.py" ]

FROM ubuntu:busybox
WORKDIR /root/
COPY --from=builder /root/something.py
CMD [ "ls","-ltr" ]
