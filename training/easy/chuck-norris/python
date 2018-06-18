import sys
import math

message = raw_input()

liste_message = []

for lettre in message:
    liste_message.append(bin(ord(lettre)))


for idx, elem in enumerate(liste_message):
    if len(list(elem)) < 9:
        elem = list(elem)
        elem[1] = "0"
        "".join(elem)
        liste_message[idx] = elem[1:]
    else:
        liste_message[idx] = elem[2:]


def changement_idx(liste):
    liste_idx_changement = [0]
    idx = 0
    while (idx < len(liste) - 1):
        idx += 1
        if (liste[idx - 1] != liste[idx]):
            liste_idx_changement.append(idx)
    liste_idx_changement.append(len(liste))
    return liste_idx_changement


def codage_chuck(liste, liste_changement):
    "fonction qui convertis le binaire en unaire"
    code = []
    idx = 0
    idx_ch = 0
    while (idx < len(liste)):
        if (liste[idx] == "1"):
            code.append("0")
        else:
            code.append("00")
        nb_char = abs(liste_changement[idx_ch] - liste_changement[idx_ch + 1])
        liste_char = []
        for i in (range(nb_char)):
            liste_char.append("0")
        code.append("".join(liste_char))
        idx_ch += 1
        idx = liste_changement[idx_ch]
    return " ".join(code)


chaine_resultat = ""
for char in liste_message:
    chaine_resultat = chaine_resultat + "".join(char)

resultat_changement = changement_idx(chaine_resultat)
print(codage_chuck(chaine_resultat, resultat_changement))
