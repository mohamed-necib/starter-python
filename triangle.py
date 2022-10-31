hauteur = int(input("Quelle hauteur souhaitez vous? "))

i = 1

while i <= hauteur:
    if i == 1:
        print(" "*(hauteur-i)+"/"+"\ ")
        i += 1
    elif i == hauteur:
        print(" "*(hauteur-i)+"/"+"_"*((i-1)*2)+"\ ")
        i += 1
    else:
        print(" "*(hauteur-i)+"/"+" "*((i-1)*2)+"\ ")
        i += 1


# ====> EXERCICE Explication pour collegue
# hauteur = int(input("Entrer une hauteur: "))

# for ligne in range(1, hauteur+1):
#     for col in range(1, 2*hauteur):
#         if ligne == hauteur or ligne+col == hauteur+1 or col-ligne == hauteur-1:
#             print("O", end="")
#         else:
#             print(end=" ")
#     print()
