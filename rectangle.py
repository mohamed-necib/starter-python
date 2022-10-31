lignes = int(input("Entrer la largeur souhaitée: "))
colonnes = int(input("Entrer la hauteur souhaitée: "))

for i in range(lignes):
    rect = "|"
    for j in range(colonnes - 2):
        if i == 0 or i == (lignes-1):
            rect += "-"
        else:
            rect += " "
    rect += "|"
    print(rect)
