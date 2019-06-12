width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

grille = [list(input()) for _ in range(height)]    # width characters, each
either 0 or .

colone, ligne = 0, 0
nb_colone, nb_ligne = width, height

liste_neuds = []

for nb in range(nb_ligne):
    for nombre in range(nb_colone):
        if grille[nb][nombre] == "0":
            liste_neuds.append([nombre, nb])

for idx, neud in enumerate(liste_neuds):
    affiche = []
    affiche.extend(neud)

    index = idx + 1
    while index < len(liste_neuds):
        if neud[1] == liste_neuds[index][1]:
            affiche.extend(liste_neuds[index])
            break
        index += 1
    else:
        affiche.extend([-1, -1])

    index2 = idx + 1
    while index2 < len(liste_neuds):
        if neud[0] == liste_neuds[index2][0]:
            affiche.extend(liste_neuds[index2])
            break
        index2 += 1
    else:
        affiche.extend([-1, -1])

    print(" ".join([str(nb) for nb in affiche]))
