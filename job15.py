# FONCTIONS ET PARAMETRES
# Créer un programme job15.py. Le programme devra contenir une fonction qui prend en
# paramètres une variable prenom et une variable nom.
# La fonction écrira “Bonjour prenom nom” dans le terminal.

# VERSION 1:
def myFunction(prenom, nom):
    print(f"Bonjour {prenom} {nom}")

myFunction("Amine", "Necib")

# VERSION 2:
prenom = str(input("Bonjour comment t'appelles tu?"))
nom = str(input("Quel est ton nom?"))

def myFunction(prenom, nom):
    print("Bonjour", prenom, nom)

myFunction(prenom, nom)
