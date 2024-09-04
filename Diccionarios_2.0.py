numbers = {1:"uno", 2:"dos", 3:"tres"} #en llaves
print(numbers)
print(numbers[1])
print(numbers[2])
print(numbers[3])
information = {"nombre":"Sebastian",
               "apellidos":"Guerra",
               "estatura":1.77,
               "esta feliz":True}
print(information)
#del information ["apellidos"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))
values = information.values()
print(values)
pairs = information.items()
print(pairs)
contacts = {"Sebastian": {"Apellido":"Guerra",
                          "Altura":1.77,
                          "Edad":34,
                          "Teléfono": 3015696015,
                          "Mes de Nacimiento":"Mayo",
                          "Serie Favorita": "Samurai X",
                          "Cancion favorita": "Mi 100% - Maxi Larghi",
                          "Comida favorita": "Hamburguesa",
                          "Viaje preferido": "Atacames",
                          "Habilidad secreta": "Volar",
                          "Hobby":"Tocar guitarra",
                          "Persona que admiras": "San Damián de Molokai",
                          "Libro favorito": "El combate espiritual",
                          "Con quien te gustaría conversar": "Santo Cura de Ars",
                          "Superpoder": "Super Fuerza",
                          "Logro que te enorgullece": "Aprender programación"},
            "Roberto": {"Apellido":"Guerra",   
                        "Altura":1.75,
                        "Edad":25,
                        "Teléfono": 3015696015,
                        "Mes de Nacimiento":"Noviembre",
                        "Serie Favorita": "Castlevania",
                        "Cancion favorita": "indeterminado",
                        "Comida favorita": "Salchipapas",
                        "Viaje preferido": "Salinas",
                        "Habilidad secreta": "invulnerabilidad",
                        "Hobby":"Trotar",
                        "Persona que admiras": "Padre Carlos Cancelado",
                        "Libro favorito": "La imitación de Cristo",
                        "Con quien te gustará conversar": "San Juan Pablo II",
                        "Superpoder": "Super Velocidad",
                        "Logro que te enorgullece": "Aprender python"}}
print(contacts)
