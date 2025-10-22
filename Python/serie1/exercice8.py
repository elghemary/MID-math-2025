nombre = int(input("Entrer un nombre: "))
premier = 0

for i in range (2, nombre):
    if nombre % i == 0:
        premier = 1
        break
if premier == 0 and nombre > 1:
    print("Le nombre est premier")
else:
    print("Le nombre n'est pas premier")