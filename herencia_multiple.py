class Mascota(object):

	def propietario(self):
		return self.propietario 

class Animal(object):

	def tipo(self):
		return self.tipo 

#clases heredan de multiples clases

class Perro(Animal,Mascota):

	def ruge(self):
		print 'El perro ladra'
		
class Gato(Animal,Mascota):

	def ruge(self):
		print 'El gato maulla'
		
el_gato = Gato()
el_perro = Perro()

el_gato.propietario = 'Juan'
el_perro.propietario = 'Jose'

el_gato.tipo = 'Felino'
el_perro.tipo = 'Canino'

print el_gato.tipo
print el_perro.tipo
print el_gato.propietario
print el_perro.propietario

