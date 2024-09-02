#menu
print("   ")
print("Seleccione la operacion que desea ingresar:")
print("   ")
print("1. convertir °F a °C")
print("2. convertir °F a  K")
print("3. convertir °C a °F")
print("4. convertir  K a °F")
print("5. convertir °C a  K")
print("6. convertir  K a °C")

#ingresando el dato numerico
print("   ")
grados = input("ingrese la operacion que desea realizar: ")

#definiciones para los calculos
def a_celcius(farenheite):
    return  round((farenheite - 32) / 1.8 ,2)  
def a_kelvin (farenheite):
    return round((farenheite + 459.67)* 5/9 ,2)
def a_farenheite (celcius):
    return round((celcius * 1.8) + 32,2)
def k_a_F (kelvin):
    return round(1.8 * (kelvin - 273.15) + 32 ,2)
def c_a_k (celcius):
    return round(celcius + 273.15 ,2)
def k_a_c (kelvin):
    return round(kelvin - 273.15 ,2)

#elif para elegir
if grados == '1':
    print("   ")
    print ("usted eligio convertir °F a °C")
    print("   ")
    num = float(input("ingrese los °F que va a convertir a °C:  "))
    print("   ")
    print ("usted tiene: ", a_celcius(num), "°C")
elif grados == '2':
    print("   ")
    print ("usted eligio convertir °F a K")
    print("   ")
    num = float(input("ingrese los °F que va a convertir a K:  "))
    print("   ")
    print ("usted tiene: ", a_kelvin(num), "K")
elif grados == '3':
    print("   ")
    print ("usted eligio convertir °C a °F")
    print("   ")
    num = float(input("ingrese los °C que va a convertir a °F:  "))
    print("   ")
    print ("usted tiene: ", a_farenheite(num), "°F")
elif grados == '4':
    print("   ")
    print ("usted eligio convertir K a °F")
    print("   ")
    num = float(input("ingrese los K que va a convertir a °F:  "))
    print("   ")
    print ("usted tiene: ", k_a_F(num), "°F")
elif grados == '5':
    print("   ")
    print ("usted eligio convertir K a °C")
    print("   ")
    num = float(input("ingrese los K que va a convertir a °C:  "))
    print("   ")
    print ("usted tiene: ", c_a_k(num), "°C")
elif grados == '6':
    print("   ")
    print ("usted eligio convertir K a °C")
    print("   ")
    num = float(input("ingrese los K que va a convertir a °C:  "))
    print("   ")
    print ("usted tiene: ", k_a_c(num), "K")
else:
    print("   ")
    print("error")
