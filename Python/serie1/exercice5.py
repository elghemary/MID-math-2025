note = float(input("Enter une note:"))

if note <= 20 and note >= 16:
    print("Très bien")
elif note < 16 and note >= 14:
    print("Bien")
elif note < 14 and note >= 12:
    print("Assez bien")
elif note < 12 and note >= 10:
    print("Passable")
elif note < 10 and note >= 0:
    print("Echec")
else:
    print("valeur invalide")