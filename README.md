# Lab Setup 2: Port Scanning & Password Cracking

## Objectives

1) Perform Network Enumeration to find target machines (Hard-Only)
2) Use provided program to ARP spoof the target 
3) Intercept traffic in between targets and find the following information
  - (Easy) Which ip addresses on the network (10.9.0.x) are communicating?
  - (Medium) What website is the user visiting?
  - (Hard) What password is being leaked in the network traffic?

## Resources

### Software

- NMAP
- ARP Spoofing Program
- Wireshark

### Other resources
- [Cheatsheet]()

## Environment setup

### Build Docker Image
```{bash}
sudo docker build -f Dockerfile -t nmaplab-victim-easy .
``` 

### Run Docker Compose
```{bash}
sudo docker compose build
sudo docker compose up
```
