#/usr/bin/env bash

## conseguir agenda
~/conky/getAgenda.sh > ~/conky/tareas

## escribir recordatorios
cat ~/conky/conky1 > ~/.conkyrc
cat ~/conky/recordatorios >> ~/.conkyrc
echo "" >> ~/.conkyrc

## escribir agenda
~/conky/buildAgenda.py ~/conky/tareas >> ~/.conkyrc
echo "" >> ~/.conkyrc

## eliminar todo rastro de posible búsqueda infiltrada peligrosa y anónima
rm ~/conky/tareas
