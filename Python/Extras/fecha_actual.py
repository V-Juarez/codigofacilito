#Es necesario importar las dependencias necesarias
from datetime import date
from datetime import datetime

#dia actual
today = date.today()

#fecha actual
now = datetime.now()

print(today)
print(now)

#date

print("El dia actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El year actual es {}".format(today.year))

#Datatime

print("El dia actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El year actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))


#new date

new_date = datetime(2020, 5, 14, 12, 30, 00, 00000)
