from scapy.all import *

def querysniff(pkt):
    if "IP" in pkt:
        ip_src = pkt["IP"].src
        ip_dst = pkt["IP"].dst
        if ip_src == "10.9.0.1" or ip_dst == "10.9.0.1":
            return
        if ip_src[:2] == "10" and ip_dst[:2] == "10":
            if "TCP" in pkt:
                sport = pkt["TCP"].sport
                dport = pkt["TCP"].dport
                print("Source IP & Port:", str(ip_src) + ":" + str(sport), "\tDestination IP & Port:", str(ip_dst) + ":" + str(dport))
            else:
                print("Source IP:", str(ip_src), "\tDestination IP:", str(ip_dst))
            raw = packet.lastlayer()
            hexdump(raw)

print("Searching for packets...")
sniff(iface="eth0", prn=querysniff)