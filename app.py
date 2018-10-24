#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from configs.log import log_print_message

def myFunction(*args):
  F = npyscreen.Form(name='My Test Application')
  F.add(npyscreen.TitleText, name="First Widget")
  F.edit()

if __name__ == '__main__':
  npyscreen.wrapper_basic(myFunction)
  log_print_message('hola \t mundo')
