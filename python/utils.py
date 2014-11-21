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

def obtenerTipo(linea):
  tipo = CONST.TITULO.TIPO.sin_tipo
  gr = re.match(".{31}(.*)", linea)
  for tupla in CONST.TITULO.TIPO.TIPOS:
    if re.match(tupla[1], gr.group(1)):
      tipo = tupla[0]
  return tipo

def obtenerHoraContenido(linea):
  hora = ""
  gr = re.match(".{12}(.{7}).{2}(.*)", linea)
  if gr.group(1) != "       ":
    hora = gr.group(1)
  contenido = gr.group(2).strip()
  return hora, contenido

def obtenerFecha(linea):
  buff = 0
  gr = re.match("\w{3} (\w{3}) (\d{2}).*", linea)
  if datetime.date.today().month > CONST.mes_i.index(gr.group(1))+1:
    buff = 1
  return datetime.date(datetime.date.today().year+buff, CONST.mes_i.index(gr.group(1))+1, int(gr.group(2)))

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
  if dias_as_is[0][0] == "No Events Found...\n":
    return []
  
  # obtener información de cada tarea.
  tareas = []
  for d in dias_as_is[:len(dias_as_is)-1]:
    fecha = obtenerFecha(d[0][:-1])
#    gr = re.match("\w{3} (\w{3}) (\d{2}).*", d[0])
#    if datetime.date.today().month > CONST.mes_i.index(gr.group(1))+1:
#      buff = 1
#    fecha = datetime.date(datetime.date.today().year+buff, CONST.mes_i.index(gr.group(1))+1, int(gr.group(2)))
    
    # obtener hora, tarea y comentario
    l = 0
    while l < len(d):
      hora, contenido = obtenerHoraContenido(d[l][:-1])
      l += 1
      tipo = obtenerTipo(d[l][:-1])
      l += 1
      
      tareas.append(Tarea(fecha, tipo, contenido, hora))
  return tareas
