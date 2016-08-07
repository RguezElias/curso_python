# validar scope

def scope_test():
	
	def do_local():
		spam = 'local spam'

	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"
	
	def do_global():
		global spam
		spam = "global spam"

spam = "Prueba spam"

do_local("asignacion local")
do_nonlocal("asignacion no local")
do_global("asignacion global")

scope_test()
print ('En scope global %s' %(spam))

