def menu():
	print("   CALCULADORA BASICA\n")
	print(" Menu de opciones: \n")
	print(" 1.- Suma")
	print(" 2.- Resta")
	print(" 3.- Multipliacion")
	print(" 4.- Division")
	op = int(input("Seleccione su opcion: "))
	return (op)


def suma():
	n1 = float(input("Ingrese un numero:  "))
	n2 = float(input("Ingrese otro numero:  "))
	R = n1 + n2
	return(R)

def resta():
	n1 = float(input("Ingrese un numero:  "))
	n2 = float(input("Ingrese otro numero:  "))
	R = n1 - n2
	return(R)



print(suma())
print(resta())