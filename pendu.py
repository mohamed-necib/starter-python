# Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
# jeu le pendu dans le terminal.
# Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
# souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
# débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
# niveau.
# Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
# ici, et afficher :
# - Le nombre de vies restantes au joueur
# - Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
# En expert, la liste n’apparaîtra pas)
# - Des “_” pour remplacer les lettres non trouvées
# - Les lettres proposées qui se trouvent dans le mot
# La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.


# importer les modules replace et aléatoire
from dataclasses import replace
import random

# ouvrir file au bon format
file = open("dico_france.txt", encoding = "ISO-8859-1")
# basculer contenu de file dans une variable data
data = file.readlines()
# remplacer caractères latin
ac1 = [data.replace ("é", "e") for data in data]
ac2 = [ac1.replace ("ê", "e") for ac1 in ac1]
ac3 = [ac2.replace ("è", "e") for ac2 in ac2]
# print(ac3)
#fermer le fichier
file.close()

# choisir un mot aléatoirement 
word=(random.choice(ac3))
print(word)

# compter le nombre de caractère du mot
char_nb=((len(word))-1)

# remplacer char_nb par autant de "_" que le mot compte de caractères
user_guess=(char_nb*"_")
print(user_guess)

list_user_guess=list(user_guess)
print(list_user_guess)

list_word=list(word)
print(list_word)

def main():
    # demander lettre à essayer
    letter=input("Quelle lettre veux-tu essayer ? ").lower
    # print lifes + char
    lifes =10
    print("Tu as ", lifes, " vies ")
    
    # tant qu'il reste des vies et que le mot n'est pas complet :
    while lifes != 0 or user_guess != word:
        print("test boucle while")

        # si la lettre est dans le mot, 
        if letter in list_word:
            print ("test if")
            
            # que index+1 est inféreur ou égal au nombre de caractères du mot, 
            #i=0
            #while i+1 <= char_nb:
            for i in range(char_nb):
                print("test boucle for")
                # si ma lettre correspond à un index du mot, je remplace le même index de list_user_guess par la lettre : 
                if letter == word[i]:
                    list_user_guess[i]=letter
                    print(list_user_guess)
                    i=+1

                # sinon ajouter letter à tried_letters
                else:
                    # enlever 1 à lifes
                    lifes -=1
                    print(lifes)
                    # créer une liste et y ajouter les lettres déjà essayées
                    tried_letters=[]
                    tried_letters.append(letter)
                    print("Voici les lettres déjà essayées : ", tried_letters)
        break
  
            # # elif lifes == 0 or guess == word :
            #     # break

            #     else:
            #     print "raté" + lifes + liste tried_letters
            #     restart()

main()




# demander level=("Bienvenue ! Quel niveau choisis-tu (1, 2 ou 3) ? ")
    # if level == "1":
        # lifes = 10
        # main()

    # if level == "2":
        # lifes = 7
        # main()

    # if level == "3":
        # lifes = 4
        # ..................




