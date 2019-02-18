FROM tomcat:8

LABEL maintainer="feiskyer@gmail.com"

RUN apt-get update && apt-get install -y procps && apt-get clean

COPY index.jsp /usr/local/tomcat/webapps/ROOT/index.jsp
