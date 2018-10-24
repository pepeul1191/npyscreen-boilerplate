#!/usr/bin/env python
# encoding: utf-8

import logging
from datetime import datetime

def log_print_message(message):
  rpta = ''
  rpta = ' ' + str(datetime.now()) + '\n \t' + message
  logging.basicConfig(filename='logs/messages.log',level=logging.DEBUG)
  logging.debug(rpta)
