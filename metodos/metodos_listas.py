lista = list ([ 1990, 1, 5, True]) # eliminé "Hola", "Sebas",
#Nos devuelve la longitud de la lista (cantidad de caracteres)
cadena = "Hola"
resultado = len(lista)
#Agregando un elemento a la lista
lista.append(4) # Agregupe el 4
#Agregando un elemento en una posicion especifica
lista.insert(2, False) #Agregué False en la posicion 2
#Agregando varios elementos a la lista
lista.extend([2014]) #Quité "Gamatech",
#Eliminando un elemento de la lista
print(len(lista))
lista.pop(0)
print(len(lista))
lista.pop(-1)
#Eliminando un elemento de la lista por su valor
#lista.remove("Gamatech")
#Ordena los elementos de la lista mientras la lista tenga número y booleanos
#lista.sort()
print(lista)
#lista.sort(reverse=True)
#Verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(5)
print(elemento_encontrado)