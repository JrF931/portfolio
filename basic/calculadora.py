#menu
print("seleccione la operacion que desea ingresar:")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")
print("5. potencia")

operacion = input("introduzca la operacion matematica que desea realizar: ")

n1 = float(input("introduzca el valor del primer numero: "))
n2 = float(input("introduzca el valor del segundo numero: "))

def suma(a, b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b
def potencia (a,b):
    return a ** b 


if operacion == '1':
    print("Resultado:", suma(n1, n2))
elif operacion == '2':
    print("resultado:", resta(n1, n2))
elif operacion == '3':
    print("resultado:", multiplicacion(n1, n2))
elif operacion == '4':
    print("resultado:", division(n1, n2))
elif operacion == '5':
    print("resultado:", potencia(n1, n2))
else:
    print ("opcion erronea")
    
    