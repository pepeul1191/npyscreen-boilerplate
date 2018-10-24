#!/usr/bin/env python
# encoding: utf-8

import npyscreen

class LoginForm(npyscreen.Form):
  def create(self):
    self.txtUser  = self.add(
      npyscreen.TitleText,
      name = 'Ususario'
    )
    self.txtPass  = self.add(
      npyscreen.PasswordEntry,
      name = 'Contraseña'
    )
    self.btnLogin = self.add(
      npyscreen.ButtonPress,
      name = 'Ingresar',
      relx = 20,
      rely= 25
    )
