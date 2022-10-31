# SANS LA METHODE SORT

def myFunction( *params ):
    myList = []

    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
            myList.sort()
        else:
            print("Attention un des paramètres n'est pas numérique")
    
    permutation = True
    passage = 0

while permutation == True:

    permutation = False
    passage = passage + 1

    for en_cours in range(0, len(myList) - passage):
        if myList[en_cours] > myList[en_cours + 1]:
            permutation = True
            # On échange les deux éléments
            myList[en_cours], myList[en_cours + 1] = \
            myList[en_cours + 1], myList[en_cours]

print(myList)

myFunction(3,6,57,9,30,42,67)