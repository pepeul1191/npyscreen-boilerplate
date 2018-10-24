#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from configs.log import log_message, log_error

def myFunction(*args):
  F = npyscreen.Form(name='My Test Application')
  myFW = F.add(npyscreen.TitleText, name = 'Nombre')
  F.edit()
  return myFW.value

if __name__ == '__main__':
  m = npyscreen.wrapper_basic(myFunction)
  log_message(m)
