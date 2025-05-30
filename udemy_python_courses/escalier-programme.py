import turtle
#! Déplacer la tortue


t= turtle.Turtle()

# for i in range(0 , 4):
#     t.forward(30)
#     t.left(90)
#     t.forward(30)
#     t.right(90)

# t.forward(10)

def escalier (taille, n):
    for i in range(0 , n):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)

        taille -= 8

t.forward(10)

escalier(30,4)
    
for i in range(0, 4):
    t.right(90)
    t.forward(30)
    t.left(90)
    t.forward(30)




turtle.done()