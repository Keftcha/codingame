r = int(raw_input())
l = int(raw_input())

liste = [r]

for _ in range(l -1):
    liste_suivante = []
    pointeur_rouge, pointeur_bleu = 0, 0
    while pointeur_bleu < len(liste):
        while (pointeur_rouge < len(liste)) and (liste[pointeur_rouge] ==
liste[pointeur_bleu]):
            pointeur_rouge += 1
        liste_suivante.extend([pointeur_rouge - pointeur_bleu,
liste[pointeur_bleu]])
        pointeur_bleu = pointeur_rouge
    liste = liste_suivante

liste = [str(nb) for nb in liste]
print(" ".join(liste))
