
#importar el modulo datetime
from datetime import datetime

#utilizando el modulo datetime
hoy = datetime.now()

print hoy
print type(hoy)

#acceso a las variables de datetime
print hoy.day
print hoy.month
print hoy.year

print hoy.hour
print hoy.minute
print hoy.second

print '%s/%s/%s' % (hoy.month, hoy.day,hoy.year)

