import sys

l = int(raw_input())
h = int(raw_input())
t = raw_input().upper()


texte = list(t)

alphabet = []

for i in range(h):
    row = raw_input()
    alphabet.append(row)

correspondance = {} # Dictionnaires des correspondance entre les numeros
d'undice de la liste et les lettres

for idx, elem in enumerate(range(65, 91)):
    correspondance[chr(elem)] = idx
correspondance[len(correspondance.keys())] = "?"

liste_indice = []
for elem in texte:
    if elem in correspondance.keys():
        liste_indice.append(correspondance[elem])
    else:
        liste_indice.append(26)


for liste in alphabet:
    for idx in liste_indice:
        affiche = []
        for nb in range(l):
            sys.stdout.write(liste[(idx*l)+nb])
    print
