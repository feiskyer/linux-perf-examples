FROM ubuntu

LABEL maintainer="feiskyer@gmail.com"

ENV STRESS_VERSION=1.0.4
RUN apt-get update && \
    apt-get install -y g++ make curl && \
    curl -o /tmp/stress-${STRESS_VERSION}.tgz https://people.seas.harvard.edu/~apw/stress/stress-${STRESS_VERSION}.tar.gz && \
    cd /tmp && tar xvf stress-${STRESS_VERSION}.tgz && \
    cd /tmp/stress-${STRESS_VERSION} && \
    ./configure && make && make install && \
    rm -rf /tmp/* && apt-get clean

ADD app /app
ADD app.c /app.c

CMD ["/app"]
