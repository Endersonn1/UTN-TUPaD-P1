# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”

print ("Hola Mundo!")

# 2) ) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.

nombre = input ("Ingrese su nombre, por favor: ")
print (f"Hola {nombre}" +"!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# a impresión por pantalla.

nombre = input ("Ingrese su nombre, por favor: ")
apellido = input (f"Hola, {nombre}" +". Ingrese su apellido, por favor: ")
edad = input ("¿Qué edad tienes? ")
lugar_residencia = input ("¿Dónde resides? ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.

radio = input("Ingrese el radio del circulo")
radio = float(radio)

pi = 3.14159

area = pi * radio * radio
perimetro =2*pi*radio
print (f"el área es  {area} y el perimetro es {perimetro}")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

segundos = input("Ingrese la cantidad de segundos: ")
segundos = int (segundos)
horas = segundos / 60 / 60
print (f"Los {segundos} segundos, son equivalentes a {horas} horas")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = input("ingrese un número")
numero = int (numero)

print(f"{numero} x 1 es igual a {numero*1}")
print(f"{numero} x 2 es igual a {numero*2}")
print(f"{numero} x 3 es igual a {numero*3}")
print(f"{numero} x 45 es igual a {numero*4}")
print(f"{numero} x 5 es igual a {numero*5}")
print(f"{numero} x 6 es igual a {numero*6}")
print(f"{numero} x 7 es igual a {numero*7}")
print(f"{numero} x 8 es igual a {numero*8}")
print(f"{numero} x 9 es igual a {numero*9}")
print(f"{numero} x 10 es igual a {numero*10}")

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = input("ingrese un número distinto de 0: ")
numero1 = int (numero1)

numero2 = input("ingrese otro número distinto de 0: ")
numero2 = int (numero2)

print(f"El resultado de la suma entre {numero1} y {numero2} es = {numero1  + numero2}")
print(f"El resultado de la división entre {numero1} y {numero2} es = {numero1  / numero2}")
print(f"El resultado de la multiplicación entre {numero1} y {numero2} es = {numero1  * numero2}")
print(f"El resultado de la resta entre {numero1} y {numero2} es = {numero1  - numero2}")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo:

peso = input("Ingrese su peso: ")
peso= float (peso)
altura = input("Ingrese su altura: ")
altura= float (altura)

print (f"Su indice de masa corporal es {peso / (altura**2)}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C equivalen a {fahrenheit} F")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero1 = float (input("ingrese un primer número: "))
numero2 = float (input("ingrese un segundo número : "))
numero3 = float (input("ingrese un tercer número : "))

print(f"El promedio de los tres números es {(numero1 + numero2 + numero3)/3}")
