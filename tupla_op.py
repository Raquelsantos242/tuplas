t = ("John", "Yoko", "Julian", "Sean", "Julian")

primeiro = t[0]
ultimo = t[3]
ultimo_tambem = t[-1]
penultimo = t[-2]

print(primeiro)
print(ultimo)

print ("")

print(ultimo_tambem)

print("")

print(primeiro, ultimo, ultimo_tambem, penultimo)

print("")

#verifica se pertence a tupla
print("Julian" in t)
print("Ringo" in t)
print("Ringo" not in t)


print("")

print("A tupla tem", len(t), "elementos")

print("")

print((1, 2, 3) > (4, 5, 6))
