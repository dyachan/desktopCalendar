#!/usr/bin/env python3

# sys.argv[1]: nombre archivo con tareas

import re, datetime, sys

#ARCHIVO_ENTRADA = "~/conky/tareas"
CANT_DIAS = 22

mes_i = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dec"]
mes_e = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
dia = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]

tipos = {"default": "${color1}", "entrega": "${color2}", "prueba": "${color3}", "otro": "${color7}"}
COLOR_HORA = "${color4}"
COLOR_FECHA_VACIA = "${color5}"
COLOR_FECHA_TAREA = "${color6}"
SEP_FECHA = " "
SEP_HORA = " "
FONT_HORA = "${font DejaVu Sans Mono:italic:size=10}"
FONT_DEFAULT = "${font}"

## del archivo obtiene la fecha, hora, contenido y tipo de tarea en una tupla en ese orden respectivo.
def obtenerTareas(archivo):
  # obtener tareas separadas por dia
  f = open(archivo, "r")
  lineas = []
  dia = -1
  while(True):
    linea = f.readline()
    if not linea:
      break
    
    if linea == "\n":
      lineas.append([])
      dia += 1
      continue
    
    lineas[dia].append(linea)
  
  # obtener tuplas de cada información de una tarea.
  tareas = []
  buff = 0
  for d in lineas[:len(lineas)-1]:
    # obtener fecha
    gr = re.match("\w{3} (\w{3}) (\d{2}).*", d[0])
    if datetime.date.today().month > mes_i.index(gr.group(1))+1:
      buff = 1
    fecha = datetime.date(datetime.date.today().year+buff, mes_i.index(gr.group(1))+1, int(gr.group(2)))
    
    # obtener hora, tarea y comentario
    l = 0
    while l < len(d):
      hora = None
      contenido = None
      tipo = None
      gr = re.match(".{12}(.{7}).{2}(.*)", d[l][:len(d[l])-1])
      if gr.group(1) != "12:00am":
        hora = gr.group(1)
      contenido = gr.group(2).strip()
      
      l += 2
      if l < len(d):
        gr = re.match(" {21}Content: (.*)", d[l][:len(d[l])-1])
        if gr != None:
          tipo = gr.group(1)
          l += 1
      
      tareas.append((fecha, hora, contenido, tipo))
  
  return tareas

## retorna un string que indica la fecha dada
def fecha2str(fecha, mes):
  s = ""
  if mes:
    s += mes_e[fecha.month-1]+" "
  else:
    s += "    "
  if fecha.day < 10:
    s += " "
  s += str(fecha.day)+" "+dia[fecha.weekday()]
  return s

## imprime una tarea determinada
def printTarea(fecha, hora, contenido, tipo, mes):
  # imprimir fecha
  if fecha:
    print(COLOR_FECHA_TAREA + fecha2str(fecha, mes) + SEP_FECHA, end="")
  else:
    print("           ", end="")
  
  # imprimir tipo
  # definir color
  if (tipo) and (tipo in tipos):
    print(tipos[tipo], end="")
  else:
    print(tipos["default"], end="")
  print(contenido, end="")
  
  # imprimir hora
  if hora:
    print(FONT_HORA + SEP_HORA + COLOR_HORA + hora + FONT_DEFAULT)
  else:
    print("")

## imprime una fecha sin tarea
def printFechaVacia(fecha, mes):
  print(COLOR_FECHA_VACIA + fecha2str(fecha, mes=mes))

## entrega las tareas en el formato esperado por conky
def formatoConky(tareas):
  delta = datetime.timedelta(1) # delta de un dia
  actual = datetime.date.today() # fecha actual a escribir
  
  t = 0 # tarea actual
  while(actual > tareas[t][0]): # saltar tareas que ya han pasado
    t += 1
  u = False # indica si se ha escrito la ultima tarea
  m = True # indica si se debe escribir el mes
  for d in range(CANT_DIAS):
    v = True # indica si hay que agregar fecha vacia
    f = True # indica si hay que escribir fecha en tarea
    while (not u) and (actual == tareas[t][0]):
      v = False
      if f:
        f = False
        printTarea(tareas[t][0], tareas[t][1], tareas[t][2], tareas[t][3], m)
        m = False
      else:
        printTarea(None, tareas[t][1], tareas[t][2], tareas[t][3], m)
        m = False
      
      t += 1
      if t >= len(tareas):
        u = True
    
    if v:
      printFechaVacia(actual, m)
      m = False
    
    if actual.weekday() == 6:
      print("")
    actual += delta
    
    if actual.day == 1:
      m = True
    
formatoConky(obtenerTareas(sys.argv[1]))

