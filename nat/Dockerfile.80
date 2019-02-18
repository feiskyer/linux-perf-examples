FROM nginx

LABEL maintainer="feiskyer@gmail.com"

ADD default.80.conf /etc/nginx/conf.d/default.conf
ADD nginx.conf /etc/nginx/nginx.conf

CMD ["/bin/sh", "-c", "echo 10485760 > /proc/sys/net/netfilter/nf_conntrack_max && nginx -g \"daemon off;\""]
