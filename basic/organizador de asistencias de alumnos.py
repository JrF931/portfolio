# Hoy falto el profesor de clases, y los chicos se organizaron para hacer la suya propia.
# 1 alumno sera el profesor y el otro sera su asistente.
# A) Pedir el nombre y la edad de los compañerps que vinieron hoy a clase y ordenar
#los datos de menor a mayor.
# B) El mayor es el profesor y el menor es el asistente: ¿Quien es quien?

#funcion para obtener a al asistente y al profesor segun la edad
def obtener_compañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range ( cantidad_de_compañeros ) :
        nombre = input ( "ingrese el nombre del compañero: " )
        edad = int ( input ( "ingrese la edad del compañero: ") )
        compañero = ( nombre, edad )
        
        #agregando la informacion a la lista
        compañeros.append ( compañero )
        
    #ordenandolos de menor a mayor segun la edad    
    compañeros.sort ( key = lambda x:x [1] )
    
    #compañeros[x]devuelve una tupla con (nombre, edad) y despues accede
    #al nombre para asi definir al asistente y al profesor
    asistente = compañeros [0] [0]
    profesor = compañeros [-1] [0]
    
    #retornamos una tupla
    return asistente, profesor

#desempaquetamos lo q nos retorna la funcion
asistente, profesor = obtener_compañeros(5)

#mostrando el resultado
print (f"el profesor es {profesor} y su asistente es: {asistente}")