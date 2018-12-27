#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from functools import wraps
from time import time
import json
import random
import uuid
import redis
from flask import Flask, jsonify

app = Flask(__name__)
redis_client = redis.StrictRedis(
    host="127.0.0.1", charset="utf-8", port=6379, db=0, decode_responses=True)


def timing(f):
    '''wrapper for elapsed_seconds'''
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        data = json.loads(result.get_data())
        data["elapsed_seconds"] = end-start
        return jsonify(data)
    return wrapper


@app.route('/')
def hello_world():
    '''handler for /'''
    return 'hello redis\n'


@app.route('/get_cache', defaults={'type_name': 'good'})
@app.route("/get_cache/<type_name>")
@timing
def get_cache(type_name):
    '''handler for /get_cache'''
    for key in redis_client.scan_iter("uuid:*"):
        value = redis_client.get(key)
        if value == type_name:
            redis_client.sadd(type_name, key[5:])
    data = list(redis_client.smembers(type_name))
    redis_client.delete(type_name)
    return jsonify({"type": type_name, 'count': len(data), 'data': data})


@app.route('/get_cache_data', defaults={'type_name': 'good'})
@app.route("/get_cache_data/<type_name>")
@timing
def get_cache_data(type_name):
    '''handler for /get_cache_data'''
    keys = [key for key in redis_client.scan_iter("uuid:*")]
    values = redis_client.mget(keys)
    matched_keys = set([keys[idx][5:] for idx, value in enumerate(values) if value == type_name ])
    return jsonify({"type": type_name, 'count': len(matched_keys), 'data': list(matched_keys)})


@app.route('/init', defaults={'num':5000})
@app.route('/init/<num>')
@timing
def initialize(num):
    '''handler for /init'''
    redis_client.flushall()
    types = ('good', 'bad', 'normal')
    sample_size = int(num)
    random_pool = random.sample(range(0, sample_size), sample_size)

    for i in range(sample_size):
        key = uuid.uuid1()
        redis_client.set('uuid:{}'.format(key), types[(random_pool[i]+i) % 3])

    return jsonify({"keys_initialized": sample_size})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
