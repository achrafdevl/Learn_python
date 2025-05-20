#! Try-Except Example
#!************* CODE *******

"""
This block asks for the user's name and age, 
tries to convert the age to an integer, 
and handles any errors if the conversion fails.
  

nom = input("Quel est votre nom ? ")
age = input("Quel est votre age ? ")

try:
    age_prochain = int(age) + 1 
except ValueError:
    print("*********waaaaaaa Erreur w3taaa9 **********")
else:
    print("Vous vous applez " + nom + ", vous avez " + str(age) + "ans")
    print("Vous vous applez " + nom + ", vous avez " + str(age_prochain) + "ans")
"""

#! While Loop Example

# n= 0 
# while n < 10 : 
#     print("allez si brahim alleeeeeeeeeeeeeeeez " + str(n))
#     n= n+1
#     print("taaaaah si brahim" )
    
"""
This block repeatedly asks for a password until the correct one ('toto') is entered.
"""
#!************* CODE *******

"""

mot_de_pass = " "
while not mot_de_pass == "toto":
    mot_de_pass = input(" what is the password ?")

print("Your password is correct. D5ole fhlak o hanina ")

"""
#!************* CODE *******

"""

age_prochain = 0
while age_prochain == 0:
    age= input("what s your age ?")
    try:
        age_prochain = int(age) + 1 
    except:
        print("******** Dkhal 3mar dylk a zmar o hanina *****")
print ("3la slamtna dirha mn gbila")

"""



""" 
Title: 💬 User Input Validation: Name and Age with Humor

This script asks the user to enter their name and age.
It makes sure the name is not left blank and the age is a valid number.
The tone is playful, mimicking casual Moroccan Arabic expressions.
"""
#!************* CODE *******
"""
# Function to ask and validate the user's age
def demande_age():
    age = 0
    while age == 0:
        age_str = input("What is your age? ")  # Prompt user for age
        try:
            age = int(age_str)  # Try to convert input to integer
        except:
            print("*******exite while*******")  # If conversion fails, print error and repeat
    print("3la slamtna dirha mn gbila")  # Congratulatory message after valid age
    return age  # Return the valid age

# Ask the user for their name
nom = input("What is your name? ")

# If the name is empty, keep asking with humor
while nom == "":
    nom = input("Waaa 3mar a zmar smytk mal mok  ")  # Funny way to insist on input
    try:
        if nom == "":
            raise ValueError("Name is empty")  # Force an exception if still empty
    except:
        print("****** ta waza mkhedma a khona  ******")  # Funny error message

print("waaaaa 3la slama")  # Greet the user after getting a valid name

# Call the function to get the age
year = demande_age()

# Final message with the user's name and age
print("Whad khone fal grouna smyto: " + nom + " fal 3mar dylo: " + str(year))
"""

"""
def demande_age():
    age = 0
    while age == 0:
        age_str = input("What is your age? ")  # Prompt user for age
        try:
            age = int(age_str)  # Try to convert input to integer
        except:
            print("*******exite while*******")  # If conversion fails, print error and repeat
    print("3la slamtna dirha mn gbila")  # Congratulatory message after valid age
    return age  # Return the valid age


def demande_nom():

    nom = input("What is your name? ")
    while nom == "":
        nom = input("Waaa 3mar a zmar smytk mal mok  ") 
        try:
            if nom == "":
                raise ValueError("Name is empty")  
        except:
            print("****** ta waza mkhedma a khona  ******") 

    print("waaaaa 3la slama")  
    return nom

# Call the function to get the age
year = demande_age()
fullName = demande_nom()

# Final message with the user's name and age
print("Whad khone fal grouna smyto: " + fullName + " fal 3mar dylo: " + str(year))


"""

#! Boolean codition


def afficher_informations_personne(nom, age):
    print()
    print("Vous vous applez" + nom +" , vous avez " + str(age) + "ans")
    print(f" vous vous applez  {nom} , vous avez {age} ans")
    print("L'an prochain vous aurez " + str(age+1) + "ans")
    print("l'an prochain vous aurez %s ans" %(age +1 ))

    # if age > 30:
    #     print("****-----Vous etes majeur------****** ")
    # elif age >= 18:
    #     print("****-----Vous etes agee------******")
    # else:
    #     print("****-----Vous etes mineur------******")
    condition = age >= 18
    print(condition)
    if condition:
        print("majeur")
    else:
        print("mineur")

def demande_age(nom_personne):
    age = 0
    while age == 0:
        age_str = input(nom_personne + "What is your age? ")  # Prompt user for age
        try:
            age = int(age_str)  # Try to convert input to integer
        except:
            print("*******exite while*******")  # If conversion fails, print error and repeat
    return age  # Return the valid age

   
def demande_nom():

    reponse_nom = ""
    while reponse_nom == "":
       
        reponse_nom= input(" your name ? ")

    print("*************")

    return reponse_nom

# nom1= demande_nom()
# nom2= demande_nom()

# age1=demande_age(nom1)
# age2 = demande_age(nom2)

# afficher_informations_personne(nom1, age1)

# print(" ***********-----------*********** ")

# afficher_informations_personne(nom2, age2)



#! For loop 

for i in range(0 , 3):
    nom = "personne" + str(i+1)
    age = demande_age(nom)
    afficher_informations_personne(nom , age )

