# FONCTIONS ET PARAMETRES 2.0
# Créer un programme job16.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini.
# La fonction écrira tous les paramètres dans le terminal.

def myFunction(*parametres):
    print("J'écris autant de paramètres que vous le souhaitez. Vos paramètres sont: ", *parametres)


myFunction("Amine", "Necib", "33 ans", "Marseille", "Algerien")
