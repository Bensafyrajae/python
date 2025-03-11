import random

def compare_random_number(user_number):
    random_number = random.randint(1, 100)

    if user_number == random_number:
        print(f"Bravo ! Les deux nombres sont {user_number}.")
    else:
        print(f" Dommage ! Votre nombre : {user_number}, Nombre aléatoire : {random_number}")

# Exemple d'utilisation :
user_input = int(input("Entrez un nombre entre 1 et 100 : "))
compare_random_number(user_input)