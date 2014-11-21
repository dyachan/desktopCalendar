# -*- coding: utf-8 -*-
#!/usr/bin/env python3


CANT_DIAS = 23

mes_i = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
mes_e = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
#dia = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sab", "Dom"]
dia = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"]

class FECHA:
  vacia = "${color2}"
  ocupado = "${color3}"
  separador = ""
  fuente = "${font}"

class TITULO:
  separador = " "
  fuente = "${font}"

  class TIPO:
    defecto = "${color4}"
    entrega = "${color5}"
    importante = "${color6}"
    otro = "${color7}"
    fraternal = "${color8}"
    sin_tipo = "${color2}"

    TIPOS = [
      (defecto, "diego.yachan@gmail.com"),
      (entrega, "entrega"),
      (importante, "importante"),
      (otro, "otro"),
      (fraternal, "elefantes")
    ]

class HORA:
  color = "${color9}"
  separador = " "
  fuente = "${font DejaVu Sans Mono:italic:size=10}"
