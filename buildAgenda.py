#!/usr/bin/env python3

# sys.argv[x]: nombre del archivo x con tareas. x>1

import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "python"))

from Agenda import Agenda
from utils import obtenerTareas
import CONST

d = obtenerTareas(sys.argv[1])
#print("Interpretada agenta personal")
#e = obtenerTareas(sys.argv[2])
#print("Interpretada agenta de entregas")
#i = obtenerTareas(sys.argv[3])
#print("Interpretada agenta importante")
#o = obtenerTareas(sys.argv[4])
#print("Interpretada agenta de varios")
#f = obtenerTareas(sys.argv[5])
#print("Interpretada agenta fraternal")

#for t in d:
#  t.showMe()
#for t in f:
#  t.showMe()

a = Agenda(22)
a.agregarTareas(d)
#a.agregarTareas(e, tipo=CONST.TITULO.TIPO.entrega)
#a.agregarTareas(i, tipo=CONST.TITULO.TIPO.importante)
#a.agregarTareas(o, tipo=CONST.TITULO.TIPO.otro)
#a.agregarTareas(f, tipo=CONST.TITULO.TIPO.fraternal)
a.toConky()
