def calcular_area_cuadrado(lado):
    return lado * lado

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_circulo(radio):
    import math
    return math.pi * radio ** 2

def main():
    print("Bienvenido a la calculadora de áreas.")
    print("1. Calcular área de un cuadrado")
    print("2. Calcular área de un rectángulo")
    print("3. Calcular área de un triángulo")
    print("4. Calcular área de un círculo")
    opcion = int(input("Por favor, elija una opción (1/2/3/4): "))

    if opcion == 1:
        lado = float(input("Ingrese la longitud de un lado del cuadrado en metros: "))
        area = calcular_area_cuadrado(lado)
        print("El área del cuadrado es:", area, "metros cuadrados.")
    elif opcion == 2:
        base = float(input("Ingrese la longitud de la base del rectángulo en metros: "))
        altura = float(input("Ingrese la altura del rectángulo en metros: "))
        area = calcular_area_rectangulo(base, altura)
        print("El área del rectángulo es:", area, "metros cuadrados.")
    elif opcion == 3:
        base = float(input("Ingrese la longitud de la base del triángulo en metros: "))
        altura = float(input("Ingrese la altura del triángulo en metros: "))
        area = calcular_area_triangulo(base, altura)
        print("El área del triángulo es:", area, "metros cuadrados.")
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo en metros: "))
        area = calcular_area_circulo(radio)
        print("El área del círculo es:", area, "metros cuadrados.")
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()

