#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from configs.log import log_message, log_error
from forms.login_form import LoginForm

def myFunction(*args):
  F = npyscreen.Form(name='My Test Application')
  myFW = F.add(npyscreen.TitleText, name = 'Nombre')
  F.edit()
  return myFW.value

def myLoginForm(*args):
    F = LoginForm(SHOW_ATX = 10, SHOW_ATY = 10)
    F.name = 'Bienvenido'
    F.edit()
    return "Created record for " + F.myName.value

if __name__ == '__main__':
  m = npyscreen.wrapper_basic(myLoginForm)
  log_message(m)
