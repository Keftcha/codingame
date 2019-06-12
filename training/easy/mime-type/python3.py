import sys
import math

n = int(input())
q = int(input())

dico_types = {}    #les clés sont les extentions et les valeurs sont les types
MIME
liste_fichiers = []

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dico_types[ext.lower()] = mt

print(dico_types, file=sys.stderr)

for i in range(q):
    fname = input()
    liste_fichiers.append(fname)

print(liste_fichiers, file=sys.stderr)

for idx, fichier in enumerate(liste_fichiers):
    liste_fichiers[idx] = fichier.split(".")

for idx, elem in enumerate(liste_fichiers):
    liste_fichiers[idx][len(elem) - 1] = liste_fichiers[idx][len(elem) -
1].lower()

print(liste_fichiers, file=sys.stderr)

for nom_fichier in liste_fichiers :
    if (len(nom_fichier) > 1):
        if ([nom_fichier[len(nom_fichier) -1]][0] in list(dico_types.keys())):
            print(dico_types[nom_fichier[len(nom_fichier) - 1]])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
