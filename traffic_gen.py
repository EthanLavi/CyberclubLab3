#! /usr/bin/env python3

from scapy.all import DNS, DNSQR, IP, sr1, UDP
from time import sleep

count = 0
while True:
    count += 1
    dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname='www.example.com'))
    answer = sr1(dns_req, verbose=0)
    print("Received answer")
    if count % 10 == 1:
        print(answer[DNS].summary())
    sleep(2)
