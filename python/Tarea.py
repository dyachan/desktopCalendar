# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import CONST

class Tarea:
  fecha = None
  tipo = None
  titulo = None
  hora = None
  
  def __init__(self, fecha, tipo, titulo, hora=""):
    self.fecha = fecha
    self.tipo = tipo
    self.titulo = titulo
    self.hora = hora
  
  def toConky(self):
    print(CONST.TITULO.fuente+self.tipo+CONST.TITULO.separador+self.titulo, end="")
    if self.hora != "":
      print(CONST.HORA.fuente+CONST.HORA.color+CONST.HORA.separador+self.hora)
    else:
      print("")
