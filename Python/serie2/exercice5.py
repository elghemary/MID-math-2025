precision = float(input('Entrer la precision'))
nombre = int(input('Entrer un nombre'))
racine2 = nombre
x0 = nombre / 2

while (abs(racine2 - x0)) > precision:
    racine2 = (x0 + nombre / x0) / 2
    x0 = racine2
print(racine2)
