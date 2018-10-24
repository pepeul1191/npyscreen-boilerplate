#!/usr/bin/env python
# encoding: utf-8

import npyscreen

def myFunction(*args):
  F = npyscreen.Form(name='My Test Application')
  F.edit()

if __name__ == '__main__':
  npyscreen.wrapper_basic(myFunction)
  print("Blink and you missed it!")
