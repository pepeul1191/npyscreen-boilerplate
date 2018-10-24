#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from config.log import add

def myFunction(*args):
  F = npyscreen.Form(name='My Test Application')
  F.add(npyscreen.TitleText, name="First Widget")
  F.edit()

if __name__ == '__main__':
  npyscreen.wrapper_basic(myFunction)
  add()
  print("Blink and you missed it!")
