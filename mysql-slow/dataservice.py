#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import time
filename = "/tmp/dataservice"


def write():
    with open(filename, "w+") as f:
        f.write("data")


def read():
    with open(filename) as f:
        return f.read()


def clean_cache():
    with open("/proc/sys/vm/drop_caches", "w") as f:
        f.write("1")

if __name__ == "__main__":
    while True:
        write()
        clean_cache()
        read()
        time.sleep(3)
