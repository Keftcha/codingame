houses = [tuple([int(coordonée) for coordonée in input().split(" ")]) for _ in
range(int(input()))]

x_min, x_max = min([house[0] for house in houses]), max([house[0] for house in
houses])

ordonnées = [house[1] for house in houses]
ordonnées.sort()
mediane = ordonnées[int(len(ordonnées)/2)]
longueur = x_max - x_min
for house in houses:
    longueur += abs(house[1] - mediane)

print(longueur)
