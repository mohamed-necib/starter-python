# Step 1 => Choix du mode Jeu ou bien Scores
# Step 2 ==> Choix du Username pour les deux joueurs
# Step 3 ===> Afficher le plateau


def morpion():
    # welcome = choix_pseudo(pseudo1, pseudo2)
    plateau = creation_base()
    plateau_final = affichage(plateau)
    symb1, symb2 = sym()
    end = ifFull(plateau, symb1, symb2)

# Creation de la base du plateau de jeu


def creation_base():
    print("Voici votre terrain de jeu")
    plateau = [["|  _", " _", " _"],
               ["|  _", " _", " _"],
               ["|  _", " _", " _"]]
    return plateau

# CETTE FONCTION DECIDE DU CHOIX DU SYMBOLE


def sym():
    symb1 = input("Joueur_1, Tu veux être les X ou les O? ")
    if symb1 == " X":
        symb2 = " O"
        print("Joueur_2, tu seras donc les O. ")
    else:
        symb2 = " X"
        print("Joueur_2, tu seras les X pour cette fois. ")
    input("Appuyer sur entrée pour continuer.")
    print("\n")
    return (symb1, symb2)

# Cette fonction demarre le jeu


def startGame(plateau, symb1, symb2, count):

    # On décide qui commence
    if count % 2 == 0:
        player = symb1
    elif count % 2 == 1:
        player = symb2
    print(player + ", c'est à ton tour de jouer. ")
    ligne = int(input("Choisis une ligne [ligne du haut:"
                      "[entrer 0, ligne du milieu: entrer 1, ligne du bas: entrer 2]"))
    colonne = int(input("Choisis une colonne:"
                        "[colonne de gauche: entrer 0, colonne du milieu: entrer 1, colonne de droite: entrer 2]"))

    # On vérifie si la séléction du joueur n'est pas hors du plateau
    while (ligne > 2 or ligne < 0) or (colonne > 2 or colonne < 0):
        horsPortée(ligne, colonne)
        ligne = int(input("Choisis une ligne [ligne du haut:"
                          "entrer 0, ligne du milieu: entrer 1, ligne du bas: entrer 2]"))
        colonne = int(input("Choisis une colonne:"
                            "colonne de gauche: entrer 0, colonne du milieu: entrer 1, colonne de droite: entrer 2]"))

    # On vérifie si notre plateau est plein
    while (plateau[ligne][colonne] == symb1) or (plateau[ligne][colonne] == symb2):
        rempli = is_empty(plateau, symb1, symb2, ligne, colonne)
        ligne = int(input("Choisis une ligne [ligne du haut:"
                          "entrer 0, ligne du milieu: entrer 1, ligne du bas: entrer 2]"))
        colonne = int(input("Choisis une colonne:"
                            "colonne de gauche: entrer 0, colonne du milieu: entrer 1, colonne de droite: entrer 2]"))

    # Reperer les symbols du joueurs sur le plateau

    if player == symb1:
        plateau[ligne][colonne] = symb1

    else:
        plateau[ligne][colonne] = symb2

    return (plateau)

# Cette fonction contrôle si le plateau est rempli


def ifFull(plateau, symb1, symb2):
    count = 1
    winner = True

    while count < 10 and winner == True:
        gaming = startGame(plateau, symb1, symb2, count)
        plateau_final = affichage(plateau)

        if count == 9:
            print("Le plateau est plein")
            if winner == True:
                print("Egalité.")

# Contrôle si on a un gagnant
        winner = greatWinner(plateau, symb1, symb2, count)
        count += 1
    if winner == False:
        print("GAME OVER, Joueur ", symb1, symb2)

# Cette fonction dit au joueur que la position séléctionnée est en dehors du plateau


def horsPortée(ligne, colonne):
    print("Hors du plateau. Choisissez un autre endroit")

# Cette fonction affiche le contour du plateau à l'initialisation du jeu


def affichage(plateau):
    lignes = len(plateau)
    colonnes = len(plateau)
    # print("   ---+-----+---")
    for i in range(lignes):
        print(plateau[i][0], " |", plateau[i][1], " |", plateau[i][2], " |")
    # print("   ---+-----+---")
    return plateau

# Fonction qui verifie si on a un gagnant


def greatWinner(plateau, symb1, symb2, count):
    winner = True
    # vérifier les lignes
    for ligne in range(0, 3):
        if (plateau[ligne][0] == plateau[ligne][1] == plateau[ligne][2] == symb1):
            winner = False
            print("Joueur_1" + symb1 + ", bravo tu es le vainqueur de la partie! ")

        elif (plateau[ligne][0] == plateau[ligne][1] == plateau[ligne][2] == symb2):
            winner = False
            print("Joueur_2" + symb2 + ", bravo tu es le vainqueur de la partie! ")

    # verifier les colonnes
    for colonne in range(0, 3):
        if (plateau[0][colonne] == plateau[1][colonne] == plateau[2][colonne] == symb1):
            winner = False
            print("Joueur_1" + symb1 + ", bravo tu es le vainqueur de la partie! ")
        elif (plateau[0][colonne] == plateau[1][colonne] == plateau[2][colonne] == symb2):
            winner = False
            print("Joueur_2" + symb2 + ", bravo tu es le vainqueur de la partie! ")

    # verifier les diagonales
    if (plateau[0][0] == plateau[1][1] == plateau[2][2] == symb1):
        winner = False
        print("Joueur_1" + symb1 + ", bravo tu es le vainqueur de la partie! ")
    elif (plateau[0][0] == plateau[1][1] == plateau[2][2] == symb2):
        winner = False
        print("Joueur_2" + symb2 + ", bravo tu es le vainqueur de la partie! ")
    elif (plateau[0][2] == plateau[1][1] == plateau[2][0] == symb1):
        winner = False
        print("Joueur_1" + symb1 + ", bravo tu es le vainqueur de la partie! ")
    elif (plateau[0][2] == plateau[1][1] == plateau[2][0] == symb2):
        winner = False
        print("Joueur_2" + symb2 + ", bravo tu es le vainqueur de la partie! ")
    return winner

# fonction qui permet de dire que la position est déja prise


def is_empty(plateau, symb1, symb2, ligne, colonne):
    print("La case choisie est déja prise, choisissez en une autre")


# CETTE FONCTION PERMET AU JOUEUR DE CHOISIR SON PSEUDO ET DE LUI ATTRIBUER LE SYMBOLE

# def choix_pseudo():
#     print("MORPION, à vous de jouer:")
#     pseudo1 = input("Joueur1 quel pseudo avez vous choisi? ")
#     pseudo2 = input("Joueur2 quel pseudo avez vous choisi? ")
#     print(f"Bonne chance {pseudo1} et {pseudo2}, que la partie commence!!!!")
#     return ()


morpion()
