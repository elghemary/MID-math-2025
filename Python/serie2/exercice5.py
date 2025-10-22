precision = float(input('Entrer la precision: '))
nombre = int(input('Entrer un nombre: '))

x0 = nombre
racine2 =  nombre / 2

while abs(racine2 - x0) > precision :
    x0 = racine2
    racine2 = (x0 + nombre / x0) / 2

# When I print racine2 it alwasy give the i+1, that's why I'm printing the x0 instead 
print(x0)