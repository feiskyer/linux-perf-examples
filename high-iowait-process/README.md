# iowait 使用率过高案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 07 和 08 篇案例。**

案例场景为多个子进程读取磁盘导致以下两种现象：

* 系统的 iowait 使用率和平均负载过高
* 大量僵尸进程

## 构建 Docker 镜像

```sh
make build
```

## 运行案例应用

```sh
make run
```

默认的运行命令为 `docker run --privileged --name=app -itd feisky/app:iowait`。

你还可以通过以下三个选项来修改磁盘读取的行为：

* `-d` 设置要读取的磁盘，默认前缀为 `/dev/sd` 或者 `/dev/xvd` 的磁盘
* `-s` 设置每次读取的数据量大小，单位为字节，默认为 67108864（也就是 64MB）
* `-c` 设置每个子进程读取的次数，默认为 20 次，也就是读取 20*64MB 数据后子进程退出

这些选项的使用方法为：

```sh
docker run --privileged --name=app -itd feisky/app:iowait /app -d /dev/sdb -s 67108864 -c 20
```

案例运行后，你可以执行 `docker logs app` 查看它的日志，正常情况下，可以看到如下的输出：

```sh
Reading data from disk /dev/sdb with buffer size 67108864 and count 20
```

## 停止应用

```sh
make clean
```
