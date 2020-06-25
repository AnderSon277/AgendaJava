def menu():
	print("\n")
	print("   CALCULADORA BASICA\n")
	print(" Que operacion desea efectuar: \n")
	print(" 1.- Suma")
	print(" 2.- Resta")
	print(" 3.- Multipliacion")
	print(" 4.- Division")
	print(" 5.- Salir")
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



n = menu()

while (n>0 and n < 6):
	if(n==1):
		num1 = float(input("Ingrese un numero:  "))
		num2 = float(input("Ingrese otro numero:  "))
		print("El resutado de la Suma es:")
		print(suma(num1,num2))
		n = menu()
	elif(n==2):
		num1 = float(input("Ingrese un numero:  "))
		num2 = float(input("Ingrese otro numero:  "))
		print("El resutado de la Resta es:")
		print(resta(num1,num2))
		n = menu()
	elif(n==3):
		num1 = float(input("Ingrese un numero:  "))
		num2 = float(input("Ingrese otro numero:  "))
		print("El resultado de la Multiplicacion es:")
		print(multiplicacion(num1,num2))
		n = menu()
	elif(n==4):
		num1 = float(input("Ingrese un numero:  "))
		num2 = float(input("Ingrese otro numero:  "))
		print("El resultado de la Division es:")
		print(division(num1,num2))
		n = menu()
	elif(n==5):
		print("Gracias por utilizar nuestra CALCULADORA BASICA :D ")
		n=-1



