# 直接 I/O 案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 17 篇案例。**

案例场景为进程以固定间隔时间读取磁盘导致以下两种现象：

* 直接 I/O 导致文件读取缓慢的问题
* 缓存命中次数与 I/O 大小不匹配的问题

## 构建 Docker 镜像

```sh
make build
```

默认的运行命令为 `docker run --privileged --name=app -itd feisky/app:io-direct`。

你还可以通过以下两个个选项来修改磁盘读取的行为：

* `-d` 设置要读取的磁盘，默认前缀为 `/dev/sd` 或者 `/dev/xvd` 的磁盘
* `-s` 设置每次读取的数据量大小，单位为字节，默认为 33554432（也就是 32MB）

这些选项的使用方法为：

```sh
docker run --privileged --name=app -itd feisky/app:io-direct /app -d /dev/sdb -s 33554432
```

案例运行后，你可以执行 `docker logs app` 查看它的日志，正常情况下，可以看到如下的输出：

```sh
Reading data from disk /dev/sdb with buffer size 33554432
```

## 运行案例应用

```sh
make run
```

## 停止应用

```sh
make clean
```
