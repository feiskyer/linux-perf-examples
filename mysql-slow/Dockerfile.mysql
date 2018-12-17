FROM mysql:5.6

LABEL maintainer="feiskyer@gmail.com"

ENV MYSQL_ALLOW_EMPTY_PASSWORD=1
ADD mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf

CMD ["mysqld", "--log_bin=on", "--sync_binlog=1"]
