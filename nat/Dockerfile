FROM nginx

LABEL maintainer="feiskyer@gmail.com"

ADD default.conf /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf

CMD ["/bin/sh", "-c", "echo 1000 > /proc/sys/net/netfilter/nf_conntrack_max && nginx -g \"daemon off;\""]
