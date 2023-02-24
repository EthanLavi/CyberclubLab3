from scapy.all import *

def querysniff(pkt):
    if IP in pkt:
        ip_src = pkt["IP"].src
        ip_dst = pkt["IP"].dst
        if pkt.haslayer("DNS") and pkt.getlayer("DNS").qr == 0:
            print(ip_src, ip_dst, pkt.getlayer("DNS").qd.qname)

sniff(iface="enp3s0", filter="port 53", prn=querysniff)
