n = int(input("Entrer un nombre: "))
factorielle = 1
i = 1
k = 0 
factoriellei = 1
factoriellej = 1
if  n == 0:
    print('1')
elif n < 0:
    print('Valeur invalid, Enter un nombre Positif')
else:
    while i <= n:
        factorielle *= i
        i += 1
        c = 1 / factorielle
    print(factorielle)
    i = 1
    while i <= n:
        factoriellei *= i
        factoriellej = factorielle / n
        c = factorielle / (factoriellei * factoriellej)
        print(c)