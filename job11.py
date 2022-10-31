# Ouvrir le fichier domains.xml
file = open('/Users/aminenecib/Desktop/Python/domains.xml')
# Lire le fichier domains.xml
readed_file = file.read()
# Filtrer en utilisant la fonction len() pour afficher en chiffre le nombre de caractère utiliser
# et split pour diviser le fichier en sous-chaînes de caractères et en ciblant par la suite le string "domain"
# filtered_file = len(readed_file.split('"domain">'))
filtered_file = readed_file.count('"domain">')
# Affichage du resultat une fois filtré
print(filtered_file)
file.close()
