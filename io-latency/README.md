# 应用程序I/O延迟案例

**《[Linux 性能优化实战](https://time.geekbang.org/column/intro/140)》第 27 篇案例。**

案例场景：

* 简单的 flask app，提供一个测试单词热度的 api。该接口会生成一批文章并分别保存到一个文件中，再逐个读取这些文件来统计目标的单词是否出现在文章中
* 应用程序接口的性能并不让人满意，I/O 延迟过大

## 构建 Docker 镜像

```sh
make build
```

## 运行案例应用

```sh
make run
```

运行后，访问 `http://<ip-address>/popularity/<word>` 就可以测试单词的热度。

## 停止应用

```sh
make clean
```
