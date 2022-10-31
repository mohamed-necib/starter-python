# LISTES
# Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
# paramètres un nombre de paramètres indéfini (uniquement des nombres).
# La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.

def undefinedArgs(*numbers):
    myList = numbers
    for x in myList:
        if x % 2 == 0:
            print(x)

undefinedArgs(0, 1, 2, 4, 5, 9, 18, 4, 7)


# Correction
def myFunction(*params):
    myList=[]
    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
        else:
            print("Attention un des paramètres n'est pas numérique")
    
    for element in myList:
        if element % 2 == 0:
            print(element)

myFunction(3,6,9,78,56,45,2)