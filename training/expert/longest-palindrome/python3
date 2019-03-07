mot = input()

liste_palin = []

def chercher(p1, p2, chaine):
    while p2 < len(chaine) and p1 >= 0 and chaine[p1] == chaine[p2]:
        p1 -= 1
        p2 += 1
    return chaine[p1+1:p2]
    
def ajouter(chaine, liste):
    if len(liste) == 0 or len(liste[0]) == len(chaine):
        liste.append(chaine)
    elif len(liste[0]) < len(chaine):
        liste.clear()
        liste.append(chaine)

for idx in range(len(mot) -2):
    if mot[idx] == mot[idx + 1]:
        ajouter(chercher(idx, idx+1, mot), liste_palin)
    elif mot[idx] == mot[idx + 2]:
        ajouter(chercher(idx, idx+2, mot), liste_palin)

[print(palin) for palin in liste_palin]
