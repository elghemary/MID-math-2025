precision = float(input('Entrer la precision'))

somme = 1
i = 1
S_i = (-1) ** i / (i + 1)**2

while abs(S_i) > precision:
    somme += S_i
    i += 1
    S_i = (-1) ** i / (i + 1)**2
    
print(somme)
