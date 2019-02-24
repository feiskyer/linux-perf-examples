#!/bin/sh

# Configure smaller mtu
ifconfig eth0 mtu 100

# Simulate packet drop
tc qdisc add dev eth0 root netem loss 30%
iptables -I INPUT -m statistic --mode random --probability 0.30 -j DROP
iptables -I OUTPUT -m statistic --mode random --probability 0.30 -j DROP

# Start nginx
nginx -g "daemon off;"