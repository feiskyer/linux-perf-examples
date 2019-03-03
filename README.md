# 《Linux 性能优化实战》案例

极客时间专栏《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》案例源码。

![introduction](images/intro.jpg)

## 部分案例列表

* [应用程序 CPU 使用率过高案例](nginx-high-cpu/README.md)
* [用户 CPU 使用率过高案例](nginx-short-process/README.md)
* [短时进程案例](short-lived-process/README.md)
* [iowait 使用率过高案例](high-iowait-process/README.md)
* [未利用系统缓存导致 I/O 缓慢案例](io-cached/README.md)
* [内存泄漏案例](mem-leak/README.md)
* [狂打日志案例](logging-app/README.md)
* [I/O延迟案例](io-latency/README.md)
* [MySQL 案例](mysql-slow/README.md)
* [Redis 延迟案例](redis-slow/README.md)
* [DNS 案例](dns/README.md)
* [网络延迟案例](network-latency/README.md)
* [NAT 案例](nat/README.md)
* [Docker 运行 Tomcat 案例](tomcat/README.md)
* [火焰图](flamegraph/README.md)

## 依赖环境

所有案例的编译运行都需要预先安装 Docker 以及必要的编译工具。以 Ubuntu 18.04 为例，可以运行以下命令来安装它们：

```sh
sudo apt-get install docker.io build-essential
```

