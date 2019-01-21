# Redis 延迟严重案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 29 篇案例。**

案例场景：

* Redis 响应延迟严重
* 系统 CPU 使用率 iowait% 高

本案例由 Python+Redis 两个容器组成。其中，Python 容器是一个基于 Flask 的应用，它会利用 Redis 来管理应用程序的缓存，并对外提供三个 HTTP 接口：

* `/`：返回 `hello redis`；
* `/init/<num>`：插入指定数量的缓存数据，如不指定数量，则默认为 5000 条；
  * 缓存的键格式为 `uuid:<uuid>`
  * 缓存的值为 `good`、`bad` 或 `normal` 三者之一
* `/get_cache/<type_name>`：查询指定值的缓存数据并返回处理时间，其中的 type_name 参数只支持 'good', 'bad' 和 'normal'。

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
