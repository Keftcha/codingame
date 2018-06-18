l = int(input())
h = int(input())
t = input().upper()

# On convertis le texte donné en liste
texte = list(t)

alphabet = []

for i in range(h):
    row = input()
    alphabet.append(row)

correspondance = {} # Dictionnaires des correspondance entre les numeros
d'undice de la liste et les lettres

for idx, elem in enumerate(range(65, 91)):
    correspondance[chr(elem)] = idx
correspondance[len(correspondance.keys())] = "?"

liste_indice = []
# On récupère les indices des lettres grace au dictionaire, on place ces
# indices dans une list
for elem in texte:
    if elem in correspondance.keys():
        liste_indice.append(correspondance[elem])
    else:
        liste_indice.append(26)


for liste in alphabet:
    for idx in liste_indice:
        for nb in range(l):
            print(liste[(idx*l)+nb], end="")
    print("")
