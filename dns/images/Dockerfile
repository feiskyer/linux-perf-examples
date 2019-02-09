FROM ubuntu

RUN apt-get update && \
    apt-get install -y dnsutils net-tools iproute2 inetutils-ping curl dnsmasq && \
    apt-get clean

ADD dnsmasq.conf /etc/dnsmasq.conf
ADD resolv.conf.dnsmasq /etc/resolv.conf.dnsmasq

