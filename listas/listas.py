to_do = ["Alistar la película",
         "Freir el maíz pira",
         "Preparar pasabocas"]
print(to_do)
numbers = [1, 2, 3, 4, "cinco"]
print(numbers)
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1, 2, 3]]
print(mix)
print(len(mix))
print("primer elemento:", mix[0])
print("elemento dos:", mix[1])
print("elemento tres:", mix[2])
print("elemento cuatro:", mix[3])
print("elemento cinco:", mix[4])
print(mix[0:2])
print(mix[:2])
print(mix)
print(mix[2:])
print(mix[2:-2])
print(mix[2:len(mix)])
mix.append(False)
print(mix)
mix.append("Sebas Guerra")
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))
numbers = [1, 2, 100, 90.45, 3, 4, 5]
print(numbers)
print("Mayor:", max(numbers))
print("Menor:", min(numbers))
del numbers [-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers
#print(numbers)