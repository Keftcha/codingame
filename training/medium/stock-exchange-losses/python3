n = int(input())
valeur = [int(i) for i in input().split()]    #v = int(i)

perte = 0

vmax = vmin = None

for nb in valeur:
    if vmax is None or vmax < nb:
        vmax = vmin = nb
        continue
    if vmin <= nb:
        continue
    vmin = nb
    diff = vmin - vmax
    if diff < perte:
        perte = diff

print(perte)
