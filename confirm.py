from scapy.all import *

def querysniff(pkt):
    if "IP" in pkt:
        ip_src = pkt["IP"].src
        ip_dst = pkt["IP"].dst
        if ip_src == "10.9.0.3" and ip_dst == "10.9.0.6":
            print("ARP spoof was successful!")
            exit(0)

sniff(iface="eth0", prn=querysniff)