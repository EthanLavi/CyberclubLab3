FROM ubuntu:latest
RUN apt update && apt install -y iproute2 iputils-ping net-tools python3 python3-pip curl
RUN pip3 install scapy

