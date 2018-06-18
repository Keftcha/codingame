houses = [tuple([int(coordonee) for coordonee in raw_input().split(" ")]) for _
in range(int(raw_input()))]

x_min, x_max = min([house[0] for house in houses]), max([house[0] for house in
houses])

ordonnees = [house[1] for house in houses]
ordonnees.sort()
mediane = ordonnees[int(len(ordonnees)/2)]
longueur = x_max - x_min
for house in houses:
    longueur += abs(house[1] - mediane)

print(longueur)
