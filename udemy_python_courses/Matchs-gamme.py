import random
min = 1
max = 5

def poser_question():
    a = random.randint(min, max)
    b = random.randint(min, max)
    question = input(f" calculate : {a} + {b} = ")
    response = int(question)
    
    if response == a + b:
        return True
    else:
        return False

points = 0

def questions():
    global points
    for i in range(0, 4):
        print(f"Q°{i+1}/4 calculate : = ")
        if poser_question():
            print(" you are win")
            points += 1
        else:
            print("you are lose")
        print("")

questions()
print(f"your points is : {points}")




import random

NOMBRE_MIN = 1
NOMBRE_MAX = 100
NB_QUESTIONS = 10


def poser_question():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0, 1)
    # 0 -> +
    # 1 -> *
    operateur_str = "+"
    if o == 1:
        operateur_str = "*"
    reponse_str = input(f"Calculez: {a} {operateur_str} {b} = ")
    reponse_int = int(reponse_str)
    calcul = a+b
    if o == 1:
        calcul = a*b
    if reponse_int == calcul:
        return True

    return False


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}:")
    if poser_question():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()

# Votre note est 2/4
print(f"Votre note est : {nb_points} / {NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Excellent!")
elif nb_points == 0:
    print("Révisez vos maths!")
elif nb_points > moyenne:
    print("Pas mal!")
else:
    print("Peut mieux faire")
