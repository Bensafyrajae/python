
nombre = int(input("Entrez un nombre : "))
longueur = int(input("Entrez la longueur de la liste : "))

multiples = []

for i in range(1, longueur + 1):
    multiples.append(nombre * i)

print(multiples)