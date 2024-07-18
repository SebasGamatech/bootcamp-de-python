# El primer tipo de dato compuesto que veremos será la lista

lista = ["Oscar Guerra", "tecnotutoriales Jheyson Galvis", True, 1.77]
print(lista[1])
lista[3] = "Sebitas"
print(lista[3])

# La tupla es una lista que no se puede modificar
tupla = ("Oscar Guerra", "tecnotutoriales Jheyson Galvis", True, 1.77)
print(tupla[1])

#tupla[0] = "Sebastián Guerra"
#print(tupla[0])

# Creando un conjunto o set
# Un conjunto no admite elementos duplicados
conjunto = {"Oscar Guerra", "tecnotutoriales Jheyson Galvis", True, 1.77, 1.77}
print(conjunto)

# Creando un diccionario
diccionario = {
    "Nombre": "Oscar",
    "Apellido" : "Guerra",
    "Estatura" : 1.77,
    "Esta feliz" : True
}

print(diccionario["Esta feliz"])
print(diccionario["Nombre"])
print(diccionario["Apellido"])
print(diccionario["Estatura"])