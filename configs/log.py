#!/usr/bin/env python
# encoding: utf-8

import logging
from datetime import datetime

def log_message(message):
  rpta = 'PRINT \n'
  rpta = rpta + ' ' + str(datetime.now()) + '\n \t' + message
  logging.basicConfig(filename = 'debug.log',level = logging.DEBUG)
  logging.debug(rpta)

def log_error(error):
  rpta = 'ERROR \n'
  rpta = rpta + ' ' + str(datetime.now()) + '\n \t' + error
  logging.basicConfig(filename = 'debug.log', level = logging.DEBUG)
  logging.debug(rpta)
