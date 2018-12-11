# 短时进程案例

**注：该案例未包含在专栏中，专栏以 [Nginx 的案例](../nginx-short-process/README.md)讲解类似问题的分析思路。**

案例场景：

* 系统的用户 CPU 使用率（usr%）过高
* 没有 CPU 使用率高的进程

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
