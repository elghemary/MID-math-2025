nombre = int(input("Entrer un nombre: "))
factorielle = 1
i = nombre
if nombre >= 1:
    while i != 1:
        factorielle *= i
        i -= 1
    print(factorielle)
elif nombre == 0:
    print('1')
else:
    print('Valeur invalid, Enter un nombre Positif')