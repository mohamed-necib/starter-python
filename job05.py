# LES BOUCLES FOR
# Créez un script job05.py
# L’utilisateur devra entrer deux valeurs en input.
# A l’aide d’une boucle for et d’une fonction system, affichez uniquement les nombres se
# trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et
# aller jusqu’à l’input 2.
# Si les deux sont égaux, le programme devra écrire “Valeurs égales”.


valeur_1 = int(input("Entrer une premiere valeur: "))
valeur_2 = int(input("Entrer une seconde valeur: "))


if valeur_1 == valeur_2:
    print("Valeurs égales")

elif valeur_1 < valeur_2:
    for i in range(valeur_1+1, valeur_2):
        print(i)

elif valeur_1 > valeur_2:
    for i in range(valeur_1-1, valeur_2, -1):
        print(i)
