#/usr/bin/env bash

readonly DIR=conky
readonly OUTPUT=.conkyrc

## conseguir agenda
if [ $# -eq 0 ]
then
  $HOME/$DIR/getAgenda.sh > $HOME/$DIR/tareas
fi

## escribir recordatorios
cat $HOME/$DIR/conky1 > $HOME/$OUTPUT
cat $HOME/$DIR/recordatorios >> $HOME/$OUTPUT
echo "" >> $HOME/$OUTPUT

## escribir agenda
if [ $# -eq 0 ]
then
  $HOME/$DIR/buildAgenda.py $HOME/$DIR/tareas > $HOME/$DIR/ultimoCal
  echo "asd"
fi
cat $HOME/$DIR/ultimoCal >> $HOME/$OUTPUT
echo "" >> $HOME/$OUTPUT

## eliminar todo rastro de posible búsqueda infiltrada peligrosa y anónima
rm -f $HOME/$DIR/tareas

