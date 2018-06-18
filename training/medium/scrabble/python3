n = int(input())

dictionaire = [input() for _ in range(n)]

lettres = list(input())

mots_possible = []

# On cherche les mots possible
for mot in dictionaire:
    liste = [char for char in lettres]
    for lettre in mot:
        if lettre in liste:
            liste.remove(lettre)
            continue
        else:
            break
    else:
        mots_possible.append(mot)

# On comptabilise les mots ayant le plus de points
points = 0
mots = []
for idx, mot in enumerate(mots_possible):
    pts = 0
    for lettre in mot:
        if lettre in ["e", "a", "i", "o", "n", "r", "t", "l", "s", "u"]:
            pts += 1
        elif lettre in ["d", "g"]:
            pts += 2
        elif lettre in ["b", "c", "m", "p"]:
            pts += 3
        elif lettre in ["f", "h", "v", "w", "y"]:
            pts += 4
        elif lettre in ["k"]:
            pts += 5
        elif lettre in ["j", "x"]:
            pts += 8
        elif lettre in ["q", "z"]:
            pts += 10

    if pts > points:
        points = pts
        index = idx

print(mots_possible[index])
