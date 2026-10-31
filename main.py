
import random


# Fonction de generation du nombre aleatoire
def tirer_nombre():
    return random.randint(10, 200)


# Fonction de saisie de la proposition
def demander_proposition():
    essai = int(input("Devinez le nombre : "))
    return essai


# Fonction de comparaison
def comparer(secret, essai):

    if essai < secret:
        return "Trop petit"

    elif essai > secret:
        return "Trop grand"

    else:
        return "Trouve"


# Fonction principale
def main():

    secret = tirer_nombre()
    tentatives = 0
    devine = False
    max_tentatives = 10

    print("================================")
    print("       JEU DE DEVINETTES")
    print("================================")
    print("Devinez un nombre entre 10 et 200")
    print("Vous avez 10 tentatives maximum.")

    while tentatives < max_tentatives and not devine:

        essai = demander_proposition()
        tentatives += 1

        resultat = comparer(secret, essai)
        print(resultat)

        if resultat == "Trouve":
            devine = True
            print("Bravo ! Vous avez trouve le nombre.")
            print("Nombre de tentatives :", tentatives)

    if not devine:
        print("Partie terminee !")
        print("Vous avez perdu.")
        print("Le nombre secret etait :", secret)


if __name__ == "__main__":
    main()

