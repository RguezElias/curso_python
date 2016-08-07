#declarar sentencias if

#recibe un numero
numero = raw_input("Numero: ")

#verifica que sea numero y convierte
if numero.isdigit():
	numero = int(numero)

	#declara sentencias if
	if numero > 11:
		print "El numero es mayor"

	#declara sentencias if else
	if numero > 11:
		print "El numero es mayor que 11"
	else:
		print "El numero es menor"

	#declara sentencias if elif else
	if numero > 11:
		print "El numero es mayor que 11"
	elif numero < 10:
		print "El numero es mayor que 10"
	else:
		print "El numero es menor"

else:
	print "tipo de dato no valido"


