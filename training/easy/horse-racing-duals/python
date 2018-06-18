n = int(raw_input())
liste_puissance = []
for i in xrange(n):
    pi = int(raw_input())
    liste_puissance.append(pi)

liste_puissance.sort()
difference = 98
idx = 0

while idx + 1 < len(liste_puissance):
     if (difference > abs(liste_puissance[idx] - liste_puissance[idx+1])):
         difference = abs(liste_puissance[idx] - liste_puissance[idx+1])
     idx += 1

print(difference)
