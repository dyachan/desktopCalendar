# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from Tarea import Tarea
import datetime, utils, re, CONST

class Agenda:
  HOY = datetime.date.today()

  dias = []
  
  def __init__(self, cant_dias):
    delta = datetime.timedelta(1) # delta de un dia
    actual = Agenda.HOY # fecha actual
    
    self.dias.append([utils.fecha2str(actual)])
    actual += delta
    for _ in range(cant_dias-1):
      if actual.day == 1:
        self.dias.append([utils.fecha2str(actual)])
      else:
        self.dias.append([utils.fecha2str(actual, mes=False)])
      actual += delta
  
  def agregarTarea(self, tarea):
    n = (tarea.fecha - Agenda.HOY).days
    if n < len(self.dias):
      self.dias[n].append(tarea)
    else:
      print("ERROR: Fecha mayor al rango ("+str(n)+")")
  
  def toConky(self):
    for dia in self.dias:
      # agregar fecha
      print(CONST.FECHA.fuente, end="")
      if len(dia) == 1:
        print(CONST.FECHA.vacia, end="")
      else:
        print(CONST.FECHA.ocupado, end="")
      print(CONST.FECHA.separador+dia[0], end="")
      
      # agregar tareas
      if len(dia[1:]) == 0:
        print("")
      else:
        dia[1].toConky()
        for tarea in dia[2:]:
          print("         ", end="")
          tarea.toConky()
      
      if re.match(".*"+CONST.dia[6], dia[0]):
        print("")
  
  # TODO: revisar eficiencia
  def agregarTareas(self, tareas, tipo=None):
    for tarea in tareas:
      if tipo != None:
        tarea.tipo = tipo
      self.agregarTarea(tarea)
