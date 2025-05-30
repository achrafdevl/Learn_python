import random

NUMBER_MIN = 1
NUMBER_MAX = 10
# NUMBER_MAGIQUE = 5
NUMBER_MAGIQUE = random.randint(NUMBER_MIN, NUMBER_MAX)
NB_VIES = 3


def demander_number(nb_min, nb_max):
    number_int = 0
    while True:
        number_str = input(f"What's the magic number between {nb_min} and {nb_max}? ")
        try:
            number_int = int(number_str)
            if number_int < nb_min or number_int > nb_max:
                print(f"ERRORE: The number must be between {nb_min} and {nb_max}.")
            else:
                return number_int
        except ValueError:
            print("Invalid input. Please enter an integer.")

"""
number = 0
vies = NB_VIES
while not number == NUMBER_MAGIQUE and vies > 0:
    print(f"stay have only {vies} chance")
    number = demander_number(NUMBER_MIN, NUMBER_MAX)
    if number == NUMBER_MAGIQUE:
        print("That's the magic number! You win! 🎉")
    elif number < NUMBER_MAGIQUE:
        print("The magic number is higher.")
        vies -= 1
    else:
        print("The magic number is lower.")
        vies -=1

if vies == 0:
    print("you are lose 😞 try again  ")
    print(f"the magique number was {NUMBER_MAGIQUE}")
    
"""
win = False

for i in range(NB_VIES):
    vies = NB_VIES - i
    print(f"You have {vies} {'chance' if vies == 1 else 'chances'} left.")
    
    number = demander_number(NUMBER_MIN, NUMBER_MAX)

    if number == NUMBER_MAGIQUE:
        print("That's the magic number! You win! 🎉")
        win = True
        break
    elif number < NUMBER_MAGIQUE:
        print("The magic number is higher.")
    else:
        print("The magic number is lower.")

if not win:
    print("You lost 😞 Try again!")
    print(f"The magic number was {NUMBER_MAGIQUE}")