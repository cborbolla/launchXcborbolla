# This is a python examples
from datetime import date

#Simple Print
print("Hola desde la consola")

# Addition
sum = 1 + 2 #=3
product = sum * 2
print("This is the addition result", sum)
print("This is the product result",product)

#Datatype
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string

type_print = type(distancia_a_alfa_centauri)
print(type_print)

#DATE
# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

print("Today's date is: " + str(date.today()))

#INPUTS OUTPUTS
print("Bienvenido al programa de bienvenid@")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("let's do some calculations")
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print("Resultado", int(first_number) + int(second_number))