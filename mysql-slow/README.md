# MySQL 慢查询案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 28 篇案例。**

案例场景：

* MySQL 查询特别慢，一个简单的查询需要 15 秒
* 系统 CPU 使用率中的 iowait% 特别高
* 磁盘 I/O 使用率接近 100%

这个案例总共由三个容器组成，包括一个 MySQL 数据库应用、一个商品搜索应用以及一个数据处理的应用。其中，商品搜索应用以 HTTP 的形式提供了一个接口：

- `/`：返回 `Index Page`；
- `/db/insert/products/<num>`：插入指定数量的商品信息；
- `/products/<product>`：查询指定商品的信息并返回处理时间。

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
