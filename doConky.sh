#!/usr/bin/env bash

readonly DIR=conky
readonly OUTPUT=.conkyrc
readonly LAST_AGENDA=ultimoCal

## conseguir agenda
if [ $# -eq 0 ]
then
  echo "Recuperando agendas"
#  $HOME/$DIR/getAgenda.sh > $HOME/$DIR/agenda
#  echo "Recuperando agenda de entregas"
#  $HOME/$DIR/getAgenda.sh entrega > $HOME/$DIR/agenda_entrega
#  echo "Recuperando agenda importante"
#  $HOME/$DIR/getAgenda.sh importante > $HOME/$DIR/agenda_importante
#  echo "Recuperando agenda de varios"
#  $HOME/$DIR/getAgenda.sh otro > $HOME/$DIR/agenda_otro
#  echo "Recuperando agenda fraternal"
#  $HOME/$DIR/getAgenda.sh elefantes > $HOME/$DIR/agenda_fraternal
fi

## escribir recordatorios
cat $HOME/$DIR/conky1 > $HOME/$OUTPUT
cat $HOME/$DIR/recordatorios >> $HOME/$OUTPUT
echo "" >> $HOME/$OUTPUT

## escribir agenda
if [ $# -eq 0 ]
then
  $HOME/$DIR/buildAgenda.py $HOME/$DIR/agenda > $HOME/$DIR/$LAST_AGENDA
#  $HOME/$DIR/buildAgenda.py $HOME/$DIR/agenda_default > $HOME/$DIR/$LAST_AGENDA
fi
cat $HOME/$DIR/$LAST_AGENDA >> $HOME/$OUTPUT
echo "" >> $HOME/$OUTPUT

## eliminar todo rastro de posible búsqueda infiltrada peligrosa y anónima
#rm -f $HOME/$DIR/agenda
