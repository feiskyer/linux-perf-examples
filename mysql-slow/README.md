# MySQL 慢查询案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 xx 篇案例。**

案例场景：

* MySQL 查询特别慢，一个简单的查询需要 15 秒
* 系统 CPU 使用率中的 iowait% 特别高
* 磁盘 I/O 使用率接近 100%

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
