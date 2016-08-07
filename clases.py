# declaracion de clases

#clase sin instrucciones

class Animal(object):
	pass

# declaracion de la clase

class Banco(object):

	#atributos de la clase

	def sucursal(self):
		return self.sucursal

	def ubicacion(self):
		return self.ubicacion

	def esta_abierto(self):
		return self.esta_abierto

	def empleados(self):
		return self.empleados

	#costructor de la clase

	def __init__(self,nombre):

		self.nombre = nombre
		self.empleados = 10

	#metodo de la clase Banco
	def dar_prestamo(self,prestamo):
		print 'tu prestamo de %s sido aprobado' %(prestamo)

	#metodo de la clase Banco sin argumentos
	def dar_ubicacion(self):
		print 'Av. Paseo Usumacinta'

#instancia banco

bancomer = Banco('BBVA')

print bancomer.nombre

#instacia con constructor

banorte = Banco('Banco Mercantil')

#asigna valor a propiedad

banorte.sucursal = 'Deportiva'

# imprime valores de propiedad

print banorte.nombre
print banorte.sucursal

print banorte.empleados
print banorte.empleados + 10

# imprime objeto del tipo banco

print banorte

#utiliza metodo de instancia

banorte.dar_prestamo('10000')
banorte.dar_ubicacion()



