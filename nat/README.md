# 网络地址转换（NAT）案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 41、42 篇案例。**

案例场景：

* Nginx 并发连接数因 NAT 降低，延迟增大

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
