import sys
import math

n = int(raw_input())
q = int(raw_input())

dico_types = {}
liste_fichiers = []

for i in range(n):
    ext, mt = raw_input().split()
    dico_types[ext.lower()] = mt

for i in range(q):
    fname = raw_input()  # One file name per line.
    liste_fichiers.append(fname)

for idx, fichier in enumerate(liste_fichiers):
    liste_fichiers[idx] = fichier.split(".")

for idx, elem in enumerate(liste_fichiers):
    liste_fichiers[idx][len(elem) - 1] = liste_fichiers[idx][len(elem) -
1].lower()

for nom_fichier in liste_fichiers :
    if (len(nom_fichier) > 1):
        if ([nom_fichier[len(nom_fichier) -1]][0] in list(dico_types.keys())):
            print(dico_types[nom_fichier[len(nom_fichier) - 1]])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
