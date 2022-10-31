# LES BOUCLES WHILE
# Créez un script job04.py
# L’utilisateur devra entrer une valeur en input.
# A l’aide d’une boucle while et d’une fonction system, affichez nombres se trouvant de 0
# (inclus) à l’input (inlus).

nombre = int(input("Entrer une valeur comprise entre 0 et 10? "))
i = 0

while i <= nombre:
    print(i)
    i += 1
