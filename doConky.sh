#!/usr/bin/env bash

readonly DIR=conky
readonly OUTPUT=.conkyrc
readonly LAST_AGENDA=ultimoCal

## conseguir agenda
if [ $# -eq 0 ]
then
  $HOME/$DIR/getAgenda.sh default > $HOME/$DIR/agenda_default
  $HOME/$DIR/getAgenda.sh elefantes > $HOME/$DIR/agenda_fraternal
fi

## escribir recordatorios
cat $HOME/$DIR/conky1 > $HOME/$OUTPUT
cat $HOME/$DIR/recordatorios >> $HOME/$OUTPUT
echo "" >> $HOME/$OUTPUT

## escribir agenda
if [ $# -eq 0 ]
then
  $HOME/$DIR/buildAgenda.py $HOME/$DIR/agenda_default $HOME/$DIR/agenda_fraternal > $HOME/$DIR/$LAST_AGENDA
#  $HOME/$DIR/buildAgenda.py $HOME/$DIR/agenda_default > $HOME/$DIR/$LAST_AGENDA
fi
cat $HOME/$DIR/$LAST_AGENDA >> $HOME/$OUTPUT
echo "" >> $HOME/$OUTPUT

## eliminar todo rastro de posible búsqueda infiltrada peligrosa y anónima
rm -f $HOME/$DIR/agenda_default $HOME/$DIR/agenda_fraternal
