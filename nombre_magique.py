NUMBER_MIN = 1
NUMBER_MAX = 10
NUMBER_MAGIQUE = 5

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

number = 0
while number != NUMBER_MAGIQUE:
    number = demander_number(NUMBER_MIN, NUMBER_MAX)
    if number == NUMBER_MAGIQUE:
        print("That's the magic number! You win! 🎉")
    elif number < NUMBER_MAGIQUE:
        print("The magic number is higher.")
    else:
        print("The magic number is lower.")
