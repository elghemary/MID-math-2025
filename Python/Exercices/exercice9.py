nombre = int(input("Entrer un nombre: "))
factorielle = 1
i = nombre
while i != 1:
    factorielle *= i
    i -= 1
print(factorielle)