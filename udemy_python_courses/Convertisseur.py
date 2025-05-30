# Pour cet exercice, vous allez créer un programme de conversion d'unités, qui sera capable de convertir des pouces (inch) en centimètres (cm), et vice-versa.

# 1 pouce = 2.54 cm
# 1 cm = 0.394 pouces
# Exemple :
# Un écran de 17 pouces de diagonale, correspond à 43,18 cm (=17*2.54)
# Voici comment votre programme doit se comporter :

# 1 - Demander à l'utilisateur si il souhaite convertir de "pouces vers cm" ou "cm vers pouces"
# 2 - Demander à l'utilisateur de rentrer la valeur à convertir (en réaffichant l'unité demandée)
# 3 - Afficher la valeur convertie (et l'unité : cm ou pouces)
# - fin du programme.


#! practice

def cm_en_pouces(cm):
    return cm / 2.54 

def pouces_en_cm(pouces):
    return pouces * 2.54

choix = input("Souhaitez-vous convertir de 'pouces vers cm' ou 'cm vers pouces' ? (entrez '1' pour pouces → cm, '2' pour cm → pouces) : ")

if choix == '1' :
    valeur = float(input("Entrez la valeur en pouces : "))
    resultat = pouces_en_cm(valeur)
    print(f"{valeur} pouces = {resultat:.2f} cm")
elif choix == '2' :
    valeur = float(input("Entrez la valeur en cm : "))
    resultat = cm_en_pouces(valeur)
    print(f"{valeur} cm = {resultat:.2f} pouces")

else:
    print("invalid input")


#! practice 2 

# Programme de conversion d'unités pouces <-> centimètres

def pouces_en_cm(pouces):
    return pouces * 2.54

def cm_en_pouces(cm):
    return cm * 0.394  # ou cm / 2.54 pour plus de précision

# 1 - Demander le sens de conversion
choix = input("Souhaitez-vous convertir de 'pouces vers cm' ou 'cm vers pouces' ?\n(entrez '1' pour pouces → cm, '2' pour cm → pouces) : ").strip()

# Vérifier le choix valide
if choix not in ['1', '2']:
    print("Choix invalide. Le programme se termine.")
else:
    while True:
        # 2 - Demander la valeur à convertir
        if choix == '1':
            valeur_str = input("Entrez la valeur en pouces (ou 'q' pour quitter) : ")
            if valeur_str.lower() == 'q':
                print("Fin du programme.")
                break
            try:
                valeur = float(valeur_str)
                resultat = pouces_en_cm(valeur)
                print(f"{valeur} pouces = {resultat:.2f} cm\n")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre (utilisez un point pour la virgule).")

        elif choix == '2':
            valeur_str = input("Entrez la valeur en cm (ou 'q' pour quitter) : ")
            if valeur_str.lower() == 'q':
                print("Fin du programme.")
                break
            try:
                valeur = float(valeur_str)
                resultat = cm_en_pouces(valeur)
                print(f"{valeur} cm = {resultat:.2f} pouces\n")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre (utilisez un point pour la virgule).")

