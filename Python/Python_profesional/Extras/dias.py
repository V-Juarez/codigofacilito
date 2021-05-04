from datetime import datetime
def current_date_format(date):
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Jumio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        message = "{} de {} de {}".format(day, month, year)

        return massage

now = date.now()
print(current_date_format(now))
