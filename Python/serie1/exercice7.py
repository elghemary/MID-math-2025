poids = float(input("Enter le poids de colis en kg:"))

if poids <= 0:
    print("valeur invalide")
elif poids <= 2 :
    print("Le prix est de 5 euros")
elif poids <= 5:
    print("Le prix est de 10 euros")   
elif poids <= 10:
    print("Le prix est de 20 euros")
elif poids > 20:
    print("Le prix est de 30 euros")
