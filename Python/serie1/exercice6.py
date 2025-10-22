print("Saisir un numero de jour de la semaine: \n")
print("1. Lundi \n2. Mardi \n3. Mercredi \n4. Jeudi \n5. Vendredi \n6. Samedi \n7. Dimanche")
jour = int(input())
if jour == 1:
    print("Lundi")
elif jour == 2:
    print("Mardi")
elif jour == 3:
    print("Mercredi")
elif jour == 4:
    print("Jeudi")
elif jour == 5:
    print("Vendredi")
elif jour == 6:
    print("Samedi")
elif jour == 7:
    print("Dimanche")
else:
    print("Numero de jour invalide")