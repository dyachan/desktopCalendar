#!/usr/bin/env python3

# sys.argv[x]: nombre del archivo x con tareas. x>1

import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "python"))

from Agenda import Agenda
from utils import obtenerTareas
import CONST

d = obtenerTareas(sys.argv[1])
f = obtenerTareas(sys.argv[2])

a = Agenda(22)
a.agregarTareas(d)
a.agregarTareas(f, tipo=CONST.TITULO.TIPO.fraternal)
a.toConky()
