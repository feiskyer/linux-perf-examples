# 应用程序狂打日志案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 26 篇案例。**

案例场景：

* 应用程序疯狂打印日志导致磁盘 I/O 瓶颈
* 等待 I/O 的 CPU 使用率（iowait%）过高

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
