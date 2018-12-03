# 应用程序 CPU 使用率过高案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 05 篇案例。**

案例场景：

* 系统的用户 CPU 使用率（usr%）过高
* 可以找出高 CPU 使用率的进程（php-fpm 进程的 CPU 使用率过高）

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
