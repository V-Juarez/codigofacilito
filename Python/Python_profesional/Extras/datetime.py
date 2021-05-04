
from datetime import datetime
from datetime import timedelta

now = datetime.now()
format = now.strftime('Dia :%d, Mes: %m, Year: %Y, Hora: %H, Minutos: %M, Segundo: %S')
print(format)

#Sumar dos dias a la fecha actual

now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

# Comparacion
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")
