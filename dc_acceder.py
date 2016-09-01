#acceder a valores del diccionario


pizza = {'tipo':'vegetariana', 'costo':150, 'caliente':True}

print pizza['tipo']

print pizza['costo']

#acceder a todos los valores de un diccionario 

print pizza.values()

#iterar valores en el diccionario

for valor in pizza:

    print valor