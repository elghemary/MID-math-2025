nombre = int(input("Entrer un nombre: "))
somme = 0
carree = 0
i = 1
if nombre >= 1:
    while i <= nombre:
        carree = i * i
        somme += carree
        i += 1
    print(somme)
else:
    print('Valeur invalide, entrer un nombre superier a 1')