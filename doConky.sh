~/conky/getAgenda.sh > ~/conky/tareas

cat ~/conky/conky1 > ~/.conkyrc
~/conky/buildAgenda.py ~/conky/tareas >> ~/.conkyrc

rm ~/conky/tareas
