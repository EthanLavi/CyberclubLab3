from scapy.all import *

def querysniff(pkt):
    if "IP" in pkt:
        ip_src = pkt["IP"].src
        ip_dst = pkt["IP"].dst
        if ip_src[:2] == "10" and ip_dst[:2] == "10":
            ls(pkt)

print("Searching for packets...")
sniff(iface="eth0", prn=querysniff)