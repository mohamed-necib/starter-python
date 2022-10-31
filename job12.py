# Step 1 => Ouvrir le fichier (path)
# Step 2 ==> Parcourir le fichier (.read())
# Step 3 ===> Compter le nombre de mots sans caractères spéciaux
# file = open('/Users/aminenecib/Desktop/Python/data.txt')
# readed_file = file.read()
# text = readed_file.replace('. ', ' ').replace(', ', ' ').replace('; ', ' ').replace('! ', ' ').replace('? ', ' ').replace(': ', ' ')
# text = len(text.split())
# file.close()


# print(text)

# CORRECTION
import re

fichier = open("data.txt", "r")
text =fichier.read()
pattern = '[a-zA-Z]+'
matches = re.findall(pattern, text)

print(len(matches))