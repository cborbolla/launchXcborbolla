# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"


#Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribir.
titulo=f"{planet} and the {name} Gravity".title()


#Ahora crea una plantilla de cadena multilínea para contener el resto de la información. En lugar de usar kilómetros, debes convertir la distancia a metros multiplicando por 1,000.
plantilla = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""

#Finalmente, usa ambas variables para unir el título y los hechos.
info = titulo.join(plantilla)

templplantillate = f"""{titulo.title()} 
{plantilla} 
""" 
print(plantilla)


# Nuevos datos muestra
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'


new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre=nombre, planeta=planeta, gravedad=gravedad))