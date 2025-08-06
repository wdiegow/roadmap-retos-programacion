#Crea ejemplos de funciones básicas que representen las diferentes posibilidades del lenguaje
#funcion sin parametros pero y sin retorno
def saludar():
    print("hola")

saludar()

#funcion con 1 parametro y con retorno
def saludar_persona(name):
    print(f"hola{name}")

saludar_persona("hola")

#funcion sin parametro con retorno
def obtener_pi():
    return 3.14159

pi = obtener_pi()  
print(pi)

#funcion con mas de 1 parametro y con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)  
print(resultado)

#funcion anidada
def funcion_externa(x):
    def funcion_interna(y): #primero se define la f y despues se la llama
        return y * 2
    resultado_interno = funcion_interna(x)
    return resultado_interno + 3

resultado = funcion_externa(5)
print(resultado)

#Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
cadena = "python" 
print(len(cadena)) #devuelve el numero de elementos de un objeto,lista,cadena o tupla

numeros = [1, 2, 3]
print(sum(numeros)) #suma todos los elementos de un iterable como listas o tupla

#Pon a prueba el concepto de variable LOCAL y GLOBAL.
var_global = 1 #mientras no este dentro de una funcion, es var global

def mi_funcion(numero):
    var_local = 2# como esta declarada adentro de una funcion entonces es local
    print("mi var global es", numero, "y mi var local es", var_local)

mi_funcion(var_global)

print("-----------------------------------------------------------------------------")

#Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
def funcion_opcional(string1, string2):
    var_local = 0
    for i in range(1,4):
        if(i % 3 == 0):
            print(string1)
        elif(i % 5 == 0):
            print(string2)
        elif(i % 3 == 0 and i % 5 == 0):
            print(string1 + string2)
        else:    
            print(i)
            var_local += 1  
    return var_local     

resultado = funcion_opcional("hola","mundo")
print("ESTE ES EL RESULTADO DE MI FUNCION OPCIONAL", resultado)
