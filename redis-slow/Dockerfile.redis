FROM redis:alpine

LABEL maintainer="feiskyer@gmail.com"

ADD redis.conf /etc/redis.conf

CMD ["redis-server", "/etc/redis.conf"]