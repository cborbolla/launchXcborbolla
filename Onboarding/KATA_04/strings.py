text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Primero, divide el texto en cada oración para trabajar con su contenido:
split_text = text.split(". ")
print(split_text)

#Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.
key_words = ["average", "temperature","distance"]

# Cree un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
for fact in split_text:
    for key_word in key_words:
        if key_word in fact:
            print(f"{key_word} is in {fact}")
    

## Ciclo para cambiar C a Celsius
text = text.replace("C","Celsius")
print(text)
#
