FROM ubuntu:latest
RUN apt update && apt install -y iproute2 iputils-ping

