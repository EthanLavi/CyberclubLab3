#! /usr/bin/env python3

from scapy.all import DNS, DNSQR, IP, send, UDP
from time import sleep

while True:
    # Sending the packet to yourself: will not return an answer but that's ok because we don't want to spam any DNS servers from LU's network
    # "Very weak attempt at DDOS" LOL
    dns_req = IP(dst='10.9.0.11')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.bank.com'))
    send(dns_req, verbose=0)
    sleep(2)
