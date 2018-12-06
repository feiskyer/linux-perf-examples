#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import random
import string
import signal
import time

from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
rHandler = RotatingFileHandler(
    "/tmp/logtest.txt", maxBytes=1024 * 1024 * 1024, backupCount=1)
rHandler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
rHandler.setFormatter(formatter)
logger.addHandler(rHandler)


def set_logging_info(signal_num, frame):
    '''Set loging level to INFO when receives SIGUSR1'''
    logger.setLevel(logging.INFO)


def set_logging_warning(signal_num, frame):
    '''Set loging level to WARNING when receives SIGUSR2'''
    logger.setLevel(logging.WARNING)


def get_message(N):
    '''Get message for logging'''
    return N * ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=1))


def write_log(size):
    '''Write logs to file'''
    message = get_message(size)
    while True:
        logger.info(message)
        time.sleep(0.1)


signal.signal(signal.SIGUSR1, set_logging_info)
signal.signal(signal.SIGUSR2, set_logging_warning)

if __name__ == '__main__':
    msg_size = 300 * 1024 * 1024
    write_log(msg_size)
