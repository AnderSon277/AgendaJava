def menu():
	print("   CALCULADORA BASICA\n")
	print(" Menu de opciones: \n")
	print(" 1.- Suma")
	print(" 2.- Resta")
	print(" 3.- Multipliacion")
	print(" 4.- Division")
	op = int(input("Seleccione su opcion: "))
	return (op)


def suma(n1,n2):
	R = n1 + n2
	return(R)

def resta(n1,n2):
	R = n1 - n2
	return(R)

def multiplicacion(n1,n2):
	R = n1 * n2
	return(R)

def division(n1,n2):
	R = n1 / n2
	return(R)



num1 = float(input("Ingrese un numero:  "))
num2 = float(input("Ingrese otro numero:  "))


print(suma(num1,num2))
print(resta(num1,num2))
print(multiplicacion(num1,num2))
print(division(num1,num2))
