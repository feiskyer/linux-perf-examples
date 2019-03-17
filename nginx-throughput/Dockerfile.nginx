FROM nginx

LABEL maintainer="feiskyer@gmail.com"

RUN apt-get update && \
    apt-get install -y procps && \
    apt-get clean

ADD app/ /app
ADD nginx.conf /etc/nginx/nginx.conf
ADD init.sh /init.sh

CMD ["/init.sh"]
