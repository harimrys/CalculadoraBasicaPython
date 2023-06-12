a = float(input("Ingresa un numero: "))
b = float(input("Ingresa otro numero: "))

def suma(a, b):
    return a + b   

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

#Se llama a las funciones con los parametros
print("La suma de los numeros es:", suma(a, b))
print("La resta de los numeros es", resta(a, b))
print("La multiplicacion de los numeros es:", multiplicacion(a, b))
print("La division de los numeros es:", division(a, b))
