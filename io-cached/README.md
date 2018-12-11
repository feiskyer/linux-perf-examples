# 直接 I/O 案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 xx 篇案例。**

案例场景：

* 直接 I/O 导致文件读取缓慢的问题
* 缓存命中次数与 I/O 大小不匹配的问题

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
