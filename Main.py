
import random


# ==========================================
# FONCTION 1 : GENERER LE NOMBRE ALEATOIRE
# ==========================================

def tirer_nombre():
    secret = random.randint(10, 200)
    return secret


# ==========================================
# FONCTION 2 : DEMANDER UNE PROPOSITION
# ==========================================

def demander_proposition():

    while True:
        try:
            essai = int(input("Devinez le nombre : "))

            if essai < 10 or essai > 200:
                print("Erreur : entrez un nombre entre 10 et 200.")
                continue

            return essai

        except ValueError:
            print("Erreur : veuillez saisir un nombre entier !")


# ==========================================
# FONCTION 3 : COMPARER LES DEUX NOMBRES
# ==========================================

def comparer(secret, essai):

    if essai < secret:
        return "Trop petit"

    elif essai > secret:
        return "Trop grand"

    else:
        return "Trouve"


# ==========================================
# FONCTION 4 : GERER UNE PARTIE
# ==========================================

def jouer():

    secret = tirer_nombre()
    tentatives = 0
    max_tentatives = 10
    devine = False

    print("\n================================")
    print("       JEU DE DEVINETTES")
    print("================================")
    print("Devinez un nombre entre 10 et 200.")
    print("Vous avez 10 tentatives maximum.\n")

    while tentatives < max_tentatives and not devine:

        essai = demander_proposition()

        tentatives += 1

        resultat = comparer(secret, essai)

        print(resultat)

        if resultat == "Trouve":

            devine = True

            print("\nBravo ! Vous avez trouve le nombre.")
            print("Nombre de tentatives :", tentatives)

        else:

            restantes = max_tentatives - tentatives
            print("Tentatives restantes :", restantes)

    if not devine:

        print("\nPartie terminee !")
        print("Vous avez perdu.")
        print("Le nombre secret etait :", secret)


# ==========================================
# FONCTION 5 : PROPOSER DE REJOUER
# ==========================================

def rejouer():

    while True:

        choix = input("\nVoulez-vous rejouer ? (oui/non) : ").lower().strip()

        if choix == "oui":
            return True

        elif choix == "non":
            return False

        else:
            print("Veuillez repondre par oui ou non.")


# ==========================================
# PROGRAMME PRINCIPAL
# ==========================================

def main():

    continuer = True

    while continuer:

        jouer()

        continuer = rejouer()

    print("\nMerci d'avoir joue !")


# ==========================================
# POINT D'ENTREE DU PROGRAMME
# ==========================================

if __name__ == "__main__":
    main()
