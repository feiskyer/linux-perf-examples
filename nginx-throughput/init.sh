#!/bin/sh
sysctl -w net.ipv4.ip_local_port_range='20000 20050'
sysctl -w net.ipv4.tcp_tw_reuse=0
sysctl -w net.ipv4.tcp_fin_timeout=3600
sysctl -w net.ipv4.tcp_max_syn_backlog=100
sysctl -w net.netfilter.nf_conntrack_max=200
sysctl -w net.core.somaxconn=10

# start nginx
nginx -g "daemon off;"
