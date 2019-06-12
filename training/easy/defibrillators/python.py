import sys
import math

def calculer_difference(point_a, point_b):
    "Fonction qui calcule la distance entre dux point. Les deux points sont de
type tuple sous la forme (x, y)"
    x = (point_b[0] - point_a[0]) * math.cos( (point_a[1] + point_b[1]) / 2)
    y = point_b[1] - point_a[1]
    distance = math.sqrt((x**2) + (y**2)) * 6371
    return distance

def remplacer_virgule(chaine):
    "Fonction qui converti une string en float"
    chaine = list(chaine)
    for idx, elem in enumerate(chaine):
        if (elem == ","):
            chaine[idx] = "."
    return (float("".join(chaine)))


lon = remplacer_virgule(raw_input())
lat = remplacer_virgule(raw_input())
n = int(raw_input())

liste_defib = []
for i in range(n):
    defib = raw_input()
    liste_defib.append(defib)

for idx, defibrilateur in enumerate(liste_defib):
    liste_defib[idx] = defibrilateur.split(";") #On convertis la chaine
d'information d'un defibrilateur en listeT

for defibrilateur in liste_defib:
    defibrilateur[4], defibrilateur[5] = remplacer_virgule(defibrilateur[4]),
remplacer_virgule(defibrilateur[5])

for defibrilateur in liste_defib:

    defibrilateur[4], defibrilateur[5] = math.radians(defibrilateur[4]),
math.radians(defibrilateur[5])


lon = math.radians(lon)
lat = math.radians(lat)

distance_mini = sys.maxint


for defibrilateur in liste_defib:
    if distance_mini > calculer_difference((lon, lat), (defibrilateur[4],
defibrilateur[5])):
        distance_mini = calculer_difference((lon, lat), (defibrilateur[4],
defibrilateur[5]))
        defib_proche = defibrilateur[1]


print(defib_proche)
