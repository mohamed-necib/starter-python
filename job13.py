# # Step 1 => nombres de lettres de l'utilisateur
# # Step 2 ==> Parcourir le file data.txt
# # Step 3 ===> Compter le nombre de mots de la taille demandée

nb_lettres = int(input("Entrer un nombre de lettres: "))

file = open('/Users/aminenecib/Desktop/Python/data.txt')
file_read = file.read()
text = file_read.replace('. ', ' ').replace(', ', ' ').replace('; ', ' ').replace('! ', ' ').replace('? ', ' ').replace(': ', ' ')
split_file = text.split()
file.close()
# print(split_file)


def nbMots(split_file):
    count = 0
    for i in split_file:
        if len(i) == nb_lettres:
            count = count + 1
    return count


# result = nbMots(split_file)
print(nbMots(split_file))


nombre = int(input("Entrer un nombre de lettres à comparer: "))

with open("data.txt", "r") as file:
    lignes = file.read()

    tableau = lignes.split()

nb_mots = 0

for i in tableau:
    if len(i) == nombre:
        nb_mots = nb_mots + 1

print(nb_mots)
