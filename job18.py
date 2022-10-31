# Step 1 => remplir myList avec mes paramètres
# Step 2 ==> Trier par ordre croissant la liste à l'aide de sort()
# Step 3 ===> Afficher la liste dans le terminal

# Version 1 ===>

def undefinedParams(*args):
    print(sorted(args))


undefinedParams(34, 26, 30, 35, 7, 21, 0)

# Version 2 ===>

# def sort_numbers(*number):
#     return number[0]

# number.sort(key=sort_numbers)
# print(number)

# sort_numbers(34, 26, 30, 28, 7, 9, 0)


# Correction ====>

# METHODE SORT

def myFunction( *params ):
    myList = []

    for param in params:
        if isinstance(param,(int)):
            myList.append(param)
            myList.sort()
        else:
            print("Attention un des paramètres n'est pas numérique")
    
    print(myList)

myFunction(3,33,45,7,9,10)


