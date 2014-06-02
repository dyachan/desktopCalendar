# -*- coding: utf-8 -*-
#!/usr/bin/env python3

from Tarea import Tarea
import CONST, re, datetime

## retorna un string que indica la fecha dada
def fecha2str(fecha, mes=True):
  s = ""
  if mes:
    s += CONST.mes_e[fecha.month-1]+" "
  else:
    s += "    "
  if fecha.day < 10:
    s += " "
  s += str(fecha.day)+" "+CONST.dia[fecha.weekday()]
  return s

def obtenerTipo(cadena):
  for tupla in CONST.TITULO.TIPO.TIPOS:
    if re.match(tupla[1], cadena):
      return tupla[0]
  return CONST.TITULO.TIPO.otro

def obtenerTareas(archivo):
  # obtener tareas separadas por dia
  f = open(archivo, "r")
  dias_as_is = []
  dia_recorrido = -1
  for linea in f.readlines():
    if linea == "\n":
      dias_as_is.append([])
      dia_recorrido += 1
      continue
    dias_as_is[dia_recorrido].append(linea)
  
  # verificar que haya algún evento
  if dias_as_is[0] == "No Events Found...\n":
    return []
  
  # obtener información de cada tarea.
  tareas = []
  buff = 0
  for d in dias_as_is[:len(dias_as_is)-1]:
    # obtener fecha
    gr = re.match("\w{3} (\w{3}) (\d{2}).*", d[0])
    if datetime.date.today().month > CONST.mes_i.index(gr.group(1))+1:
      buff = 1
    fecha = datetime.date(datetime.date.today().year+buff, CONST.mes_i.index(gr.group(1))+1, int(gr.group(2)))
    
    # obtener hora, tarea y comentario
    l = 0
    while l < len(d):
      hora = ""
      contenido = ""
      tipo = CONST.TITULO.TIPO.defecto
      
      gr = re.match(".{12}(.{7}).{2}(.*)", d[l][:len(d[l])-1])
      if gr.group(1) != "12:00am":
        hora = gr.group(1)
      contenido = gr.group(2).strip()
      
      l += 2
      if l < len(d):
        gr = re.match(" {21}Content: (.*)", d[l][:len(d[l])-1])
        if gr != None:
          tipo = obtenerTipo(gr.group(1))
          l += 1
      
      tareas.append(Tarea(fecha, tipo, contenido, hora))
  return tareas
