class Animal(object):

	def tipo(self):
		return self.tipo 

class Perro(Animal):

	def ruge(self):
		print 'El perro ladra'
		
class Gato(Animal):

	def ruge(self):
		print 'El gato maulla'
		
el_gato = Gato()
el_perro = Perro()

el_gato.tipo = 'Felino'
el_perro.tipo = 'Canino'

print el_gato.tipo
print el_perro.tipo

el_gato.ruge()
el_perro.ruge()

