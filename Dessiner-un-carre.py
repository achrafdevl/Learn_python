import turtle
#! Déplacer la tortue


t= turtle.Turtle()




def carre (taille):
    for i in range (0,4):
        t.forward(taille)
        t.left(90)


def carres (taille_depart, nb):
    for i in range(0 , nb):
        taille = ((i+1)*2)*taille_depart
        carre(taille)



carre(10)
carres(10 , 4)






turtle.done()