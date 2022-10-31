# First step => Création d'un fichier + ajout du texte à l'intérieur
# Second step ==> Modification du fichier (ajout du texte)
# Third step ===> Lecture du fichier dans le terminal
text = str(input("Entrer votre texte: "))

# Création du fichier
file = open("output.txt", "x")
# Ajout contenu dans le fichier
file.write(text)
# Ouverture du fichier
file = open("output.txt", "r")
# Déclaration variable fichier ouvert = fichier.read()
opened_file = file.read()
# Affichage du contenu dans le terminal
print(opened_file)
