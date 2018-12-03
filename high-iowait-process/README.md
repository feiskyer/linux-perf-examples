# iowait 使用率过高案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 07 和 08 篇案例。**

案例场景：

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

## 停止应用

```sh
make clean
```
