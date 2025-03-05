#ARIMETICOS
resultado = 1 + 2 #SUMA
resultado = 1 - 2 #RESTA
resultado = 1 * 2 #MULTIPLICACION
resultado = 1 / 2 #DIVISION (devuelve un flotante)
resultado = 1 // 2 #DIVISION ENTERA (devuelve el cociente sin decimal)
resultado = 1 % 2 #MODULO (devuelve el residuo)
resultado = 1 ** 2 #EXPONENCIACION (eleva el 1er operando a la valor del 2do operando)
#LOGICOS------------------------------------------------------------------------------
resultado = (1 > 2) and (2 < 1) #AND (true si ambas son iguales)
resultado = (1 > 2) or (2 < 1) #OR (true si almenos una de las expresiones es verdad)
resultado = not (2 < 1) #NOT (invierte el valor de la expresion)
#COMPARACION--------------------------------------------------------------------------
resultado = (5 == 5) #IGUAL (true si los dos son iguales)
resultado = (5 != 5) #DISTINTO (true si los dos son distintos)
resultado = (5 > 5) #MAYOR QUE (true si el 1ro es mayor que el 2do)
resultado = (5 < 5) #MENOR QUE (true si el 1ro es menor que el 2do)
resultado = (5 >= 5) #MAYOR IGUAL (true si el 1ro es mayor o igual que el 2do)
resultado = (5 <= 5) #MENOR IGUAL (true si el 1ro es menor o igual que el 2do)
#ASIGNACION---------------------------------------------------------------------------
resultado = 10 #ASIGNACION (asigna el valor del operando de la derecha a la izquierda)
resultado += 10 #ASIGANCION DE SUMA (suma el valor del operando de la derecha con el 
#de la izquierda y asigna el resultado a la variable de la izquierda)
resultado -= 10 #ASIGNACION DE RESTA (resta el valor del operando de la izquierda con
# el de la izquierda y asigna el resulatdo a la variable de la izquierda)
resultado *= 10 #ASIGNACION DE MULTIPLICACION (multiplica el valor del operando de la 
# derecha con el de la derecha y asigna el resultado a la variable de la izquierda)
resultado /= 10 #ASIGNACION DE DIVISION (divide el valor del operando de la izquierda
# con el de la derecha y asigna el resultado a la variable de la izquierda)
resultado //= 10 #ASIGNACION DE DIVISION ENTERA (realiza la division ENTERA del 
# valor del operando de la izquierda por el valor del de la derecha y asigna el
# resultado a la variable de la izquierda)
resultado %= 10 #ASIGNACION DEL MODULO (calcula el residuo de la division del 
# operando de la izquierda con el de la derecha y asigna el resultado a la variable
# de la izquierda)
resultado **= 10 #ASIGANCION DE EXPONENCIACION (eleva el operando de la izquierda 
# a la potencia del operando de la derecha y asigna el resualtado a la varibale 
# de la izquierda)
#IDENTIDAD-------------------------------------------------------------------------
# "is" (devuelve true si ambas variables apuntan al mismo objeto en memoria)
a = [1, 2, 3]
b = a
resultado = (a is b)
# "is not" (devuelve true si ambas variables no apuntan al mismo objeto en memoria)
a = [1, 2, 3]
b = [1, 2, 3]
resultado = (a is not b) 
#PERTENECIA------------------------------------------------------------------------
# "in" (devuelve true si el valor espesificado se encuantra en la secuencia)
lista = [1, 2, 3, 4, 5]
resultado = (1 in lista) # sera true
# "not in" (devuelve true si el valor espesificado no se encuantra en la secuencia)
lista = [1, 2, 3, 4, 5]
resultado = (6 not in lista) # sera true
#BITS-----------------------------------------------------------------------------
resultado = 5 & 3 #AND (&) 
# resultado es 1 (0101 & 0011 = 0001)
resultado = 5 | 3 #OR (|)
# resultado es 7 (0101 | 0011 = 0111)
resultado = 5 ^ 3 #XOR (^)
# resultado es 6 (0101 ^ 0011 = 0110)
resultado = 5 >> 3 #DEZPLAZAMIENTO A LA DERECHA (>>)
# resultado es 2 (0101 se convierte en 0010)
resultado = 5 << 3 # DEZPLAZAMIENTO A LA IZQUIERDA (<<)
# resultado es 10 (0101 se convierte en 1010)
resultado = ~5 #NOT A NIVEL DE BITS 
# resultado es -6 (en binario, invierte los bits de 0101)
#OPERADOR DE CONCATENACION-------------------------------------------------------
cadena1 = "buenos"
cadena2 = "dias"
resultado = cadena1 + cadena2 # el (+) tambien se usa para concatenar cadenas
#OPERADOR DE REPETICION----------------------------------------------------------
cadena1 = "hola! " *3 # resultado es "Hola! Hola! Hola! "
#OPERADOR TERNARIO---------------------------------------------------------------
resultado = "mayor" if a > b else "menor" #asigna mayor si a es mayor de lo 
#contrario menor
#OPERADOR DE DESEMPAQUETAMIENTO--------------------------------------------------
# el operador * se puede usar para desmpaquetar listas o tuplas
lista = [1, 2, 3]
#print(*lista) #salida 1 2 3

#ESTRUCTURAS DE CONTROL CONDICIONALES
var1 = 16
var2 = 26
if var1 > var2:
    print("IF: var1 es mayor que var2")
elif var2 > var1:
    print("IF:",var2, "es mayor que" , var1)
else: 
    print("IF: ",var1 + "y" , var2 , "son iguales")
#ESTRUCTURAS DE CONTROL DE BUCLES: for, while
for i in range(var1, 0, -1): 
    if i == 1:
        print("FOR: var1 es = ", 1) 
while var2 != var1:        
    print("WHILE: var2 es diferente de var1")
    var2 = var1 
#ESTRUCTURAS DE CONTROL DE SALIDA: break,continue y return 
for i in range(10):
    if i == 5:
        print("BREAK: cuando llegue a 5")
        break

for i in range(10):
    if i % 2 == 0:
        continue  # Esto saltará a la siguiente iteración, pero no hay código después
    print("CONTINUE: Número impar:", i)
#return 
def function(a, b):
    try: # Intentamos realizar la operación
        c = a + b
        return c
    except TypeError:# Manejo de excepciones si hay un error de tipo
        print("Error: Ambos argumentos deben ser números.")
        return None
    finally:
        # Esto sej ecutará independientemente de si ocurrió una excepción o no
        print("Ejecución de la función finalizada.")

# Llamada a la función
resultado = function(10, 30)
print("Resultado:", resultado)

# Ejemplo con un error
resultado = function(10, "30")  # Esto generará un TypeError
print("Resultado:", resultado)

#programa que imprima por consola todos los números comprendidos
#entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3
for n in range(10, 56):
    if n % 2 == 0 and n != 16 and n % 3 != 0:
        print(n)