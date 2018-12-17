#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import pymysql
import random
import string
import time
from flask import Flask

config = {
    "host": "127.0.0.1",
    "user": "root",
    "port": 3306,
    "password": "",
    "database": "test"
}


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route("/sleep/<num>")
def sleep(num):
    time.sleep(int(num))
    return "sleep " + num + "\n"


@app.route('/db/<table>/count')
def select(table):
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "SELECT count(*) FROM " + table
    cursor.execute(sql)
    data = cursor.fetchone()
    return str(data[0]) + "\n"


@app.route('/products/<product>')
def products(product):
    start = time.time()
    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "select * from products where productName='%s'" % product
    cursor.execute(sql)
    data = cursor.fetchall()
    elapsed = (time.time() - start)
    return "Got data: " + str(data) + " in " + str(elapsed) + " sec \n"


@app.route('/db/insert/products/<num>')
def insert_products(num):
    values = []
    i = 0
    while i < int(num):
        i += 1
        productCode = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10240))
        productName = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10240))
        productLine = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10240))
        productScale = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10240))
        productVendor = ''.join(random.choices(
            string.ascii_letters + string.digits, k=10240))
        productDescription = ''.join(random.sample(
            string.ascii_letters + string.digits, 8))
        quantityInStock = random.randint(1, 1000)
        buyPrice = random.uniform(1.0, 10000.0)
        MSRP = random.uniform(10.0, 20000.0)

        value = (i, productCode, productName, productLine, productScale,
                 productVendor, productDescription, quantityInStock, buyPrice, MSRP)
        values.append(value)

    db = pymysql.connect(**config)
    cursor = db.cursor()
    sql = "INSERT INTO products (id, productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, values)
    db.commit()
    cursor.close()
    return 'insert ' + num + ' lines' + "\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
