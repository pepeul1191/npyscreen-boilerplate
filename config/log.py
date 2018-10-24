#!/usr/bin/env python
# encoding: utf-8

import logging


def add():
  logging.basicConfig(filename='example.log',level=logging.DEBUG)
  logging.debug('This message should go to the log file')
