#/usr/bin/env bash
cat ~/conky/conky1 > ~/.conkyrc
cat ~/conky/recordatorios >> ~/.conkyrc
echo "" >> ~/.conkyrc

~/conky/getAgenda.sh > ~/conky/tareas
~/conky/buildAgenda.py ~/conky/tareas >> ~/.conkyrc
echo "" >> ~/.conkyrc

rm ~/conky/tareas
