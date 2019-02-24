FROM nginx

LABEL maintainer="feiskyer@gmail.com"

RUN apt-get update && \
    apt-get install -y iproute net-tools iputils-ping iptables tcpdump sysstat ethtool && \
    apt-get clean

ADD start.sh /start.sh

CMD ["/start.sh"]