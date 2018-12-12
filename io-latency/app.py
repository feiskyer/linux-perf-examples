#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import uuid
import random
import shutil
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, jsonify

app = Flask(__name__)


def validate(word, sentence):
    return word in sentence


def generate_article():
    s_nouns = [
        "A dude", "My mom", "The king", "Some guy", "A cat with rabies",
        "A sloth", "Your homie", "This cool guy my gardener met yesterday",
        "Superman"
    ]
    p_nouns = [
        "These dudes", "Both of my moms", "All the kings of the world",
        "Some guys", "All of a cattery's cats",
        "The multitude of sloths living under your bed", "Your homies",
        "Like, these, like, all these people", "Supermen"
    ]
    s_verbs = [
        "eats", "kicks", "gives", "treats", "meets with", "creates", "hacks",
        "configures", "spies on", "retards", "meows on", "flees from",
        "tries to automate", "explodes"
    ]
    infinitives = [
        "to make a pie.", "for no apparent reason.",
        "because the sky is green.", "for a disease.",
        "to be able to make toast explode.", "to know more about archeology."
    ]
    sentence = '{} {} {} {}'.format(
        random.choice(s_nouns), random.choice(s_verbs),
        random.choice(s_nouns).lower() or random.choice(p_nouns).lower(),
        random.choice(infinitives))
    return '\n'.join([sentence for i in range(50000)])


@app.route('/')
def hello_world():
    return 'hello world'


@app.route("/popularity/<word>")
def word_popularity(word):
    dir_path = '/tmp/{}'.format(uuid.uuid1())
    count = 0
    sample_size = 1000

    def save_to_file(file_name, content):
        with open(file_name, 'w') as f:
            f.write(content)

    try:
        # initial directory firstly
        os.mkdir(dir_path)

        # save article to files
        for i in range(sample_size):
            file_name = '{}/{}.txt'.format(dir_path, i)
            article = generate_article()
            save_to_file(file_name, article)

        # count word popularity
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                with open('{}/{}'.format(dir_path, file_name)) as f:
                    if validate(word, f.read()):
                        count += 1
    finally:
        # clean files
        shutil.rmtree(dir_path, ignore_errors=True)

    return jsonify({'popularity': count / sample_size * 100, 'word': word})


@app.route("/popular/<word>")
def word_popular(word):
    count = 0
    sample_size = 1000
    articles = []

    try:
        for i in range(sample_size):
            articles.append(generate_article())

        for article in articles:
            if validate(word, article):
                count += 1
    finally:
        pass

    return jsonify({'popularity': count / sample_size * 100, 'word': word})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
