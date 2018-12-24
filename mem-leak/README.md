# 内存泄漏案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 18 篇案例。**

案例场景：

* 应用程序存在内存泄漏
* memleak 工具无法获得应用程序调用栈

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
