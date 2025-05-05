# 1. Escribir un programa que solicite la edad del usuario.
# Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

MAYOR_EDAD = 18
edad_usuario = int(input("Ingrese su edad"))

if edad_usuario >= MAYOR_EDAD:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.") 

# 2. Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

NOTA_APROBAR = 6
nota_usuario = float(input("Ingrese su nota"))

if nota_usuario >= NOTA_APROBAR:
    print("Aprobado")
else:
    print("Desaprobado") # De lo contrario, se imprimirá "Desaprobado"

# 3. Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en 
# pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num_ingresado = int(input("Ingrese un número entero:"))

if num_ingresado % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.") 
    
# 4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: 
# ●​ Niño/a: menor de 12 años. ●​ Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ●​ Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad:"))

CATEGORIA_NINIO = range(0, 12)
CATEGORIA_ADOLESCENTE = range(12, 18)
CATEGORIA_JOVENADULTO = range(18, 30)

if edad in CATEGORIA_NINIO:
    print("Usted es un niño.") 
elif edad in CATEGORIA_ADOLESCENTE:
    print("Usted es un adolescente.") 
elif edad in CATEGORIA_JOVENADULTO:
    print("Usted es un adulto joven.") 
else:
    print("Usted es un adulto.") 

# 5. Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña
# de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor,
# ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que 
# tiene un iterable tal como una lista o un string.

contraseña = str(input("Ingrese su contraseña: "))

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.") 

#6. Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo,
#  negativo o no hay sesgo. Imprimir el resultado por pantalla. Definir la lista numeros_aleatorios de la siguiente forma: 

from statistics import mode, median, mean
import random

num_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(num_aleatorios)
mediana = median(num_aleatorios)
media = mean(num_aleatorios)

print(f"La media es {media}, la mediana es {mediana} y la moda {moda}.")

if media > mediana:
    print("El sesgo es positivo o a la derecha.")
elif media < mediana:
    print("El sesgo es negativo o a la izquierda.")
else:
    print("No hay sesgo.")

# 7. Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir 
# el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una frase o palabra: ")

if frase [-1].lower() in "aeiou":
    frase += "!"
    print("Resultado:", frase)
else:
    print("Resultado:", frase)

# 8. Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1.​ Si quiere su nombre en mayúsculas. 
# Por ejemplo: PEDRO. 2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla.
#  Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = str(input("Ingresá tu nombre:"))

print("Ahora ingrese 1, 2 o 3 según la opción que desee:")
print("1. Si querés que tu nombre aparezca en mayúsculas.")
print("2. Si querés que tu nombre aparezca en minúsculas.")
print("3. Si querés que tu nombre aparezca capitalizado (primera letra en mayúscula).")

opcion = int(input("Ingrese su opción (1, 2 o 3): "))

if opcion == 1:
    print(nombre.upper())

elif opcion == 2:
    print(nombre.lower())

elif opcion == 3:
    print(nombre.title())

else:
    print("opción no valida. Elija 1, 2 o 3")

# 9. Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter 
# e imprima el resultado por pantalla: ●​ Menor que 3: "Muy leve" (imperceptible). ●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible). 
# ●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). 
# ●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). 
# ●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
# ●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Bríndame la magnitud del terremoto: "))

if magnitud < 3:
    print(f"Según la escala de Richter, la magnitud {magnitud} indica que el terremoto es muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print(f"Según la escala de Richter, la magnitud {magnitud} indica que el terremoto es leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print(f"Según la escala de Richter, la magnitud {magnitud} indica que el terremoto es moderado (sentido por las personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print(f"Según la escala de Richter, la magnitud {magnitud} indica que el terremoto es fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print(f"Según la escala de Richter, la magnitud {magnitud} indica que el terremoto es muy fuerte (puede causar daños significativos).")
else:
    print(f"Según la escala de Richter, la magnitud {magnitud} indica que el terremoto es extremo (puede causar graves daños a gran escala).")

# 10. Estación del año: 

hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ").upper()
mes = int(input("¿Qué mes es? Ingrese el número correspondiente al mes (1 a 12): "))
dia = int(input("¿Qué día del mes es? (1 a 31): "))

if mes < 1 or mes > 12:
    print("Mes inválido. Debe estar entre 1 y 12.")
elif dia < 1 or dia > 31:
    print("Día inválido. Debe estar entre 1 y 31.")
else:
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
    elif hemisferio == "S":
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion = "Primavera"
    else:
        estacion = "Hemisferio no válido"

    print(f"La estación del año es: {estacion}")