x = raw_input()
n = int(raw_input())

plaque_liste = x.split("-")
plaque_liste[0], plaque_liste[2] = list(plaque_liste[0]), list(plaque_liste[2])
plaque_liste[1] = int(plaque_liste[1])

plaque_liste[0][0] = ord(plaque_liste[0][0])
plaque_liste[0][1] = ord(plaque_liste[0][1])
plaque_liste[2][0] = ord(plaque_liste[2][0])
plaque_liste[2][1] = ord(plaque_liste[2][1])

a = 0

if n > 17558424:
    a = n // 17558424
    for elem in range(a):
        plaque_liste[0][0] += 1

n = n - a*17558424

if n > 675324:
    a = n // 675324
    for elem in range(a):
        plaque_liste[0][1] += 1
        if plaque_liste[0][1] > 90:
            plaque_liste[0][0] += 1
            plaque_liste[0][1] = 65

n = n - a*675324

if n > 25974:
    a = n // 25974
    for elem in range(a):
        plaque_liste[2][0] += 1
        if plaque_liste[2][0] > 90:
            plaque_liste[0][1] += 1
            plaque_liste[2][0] = 65

n = n - a*25974

if n > 999:
    a = n // 999
    for elem in range(a):
        plaque_liste[2][1] += 1
        if plaque_liste[2][1] > 90:
            plaque_liste[2][0] += 1
            plaque_liste[2][1] = 65


n = n - a*999

for elem in range(n):
    plaque_liste[1] += 1
    if plaque_liste[1] > 999 :
        plaque_liste[2][1] += 1
        plaque_liste[1] = 1
    if plaque_liste[2][1] > 90:
        plaque_liste[2][0] += 1
        plaque_liste[2][1] = 65
    if plaque_liste[2][0] > 90:
        plaque_liste[0][1] += 1
        plaque_liste[2][0] = 65
    if plaque_liste[0][1] > 90:
        plaque_liste[0][0] += 1
        plaque_liste[0][1] = 65

plaque_liste[0][0] = chr(plaque_liste[0][0])
plaque_liste[0][1] = chr(plaque_liste[0][1])
plaque_liste[2][0] = chr(plaque_liste[2][0])
plaque_liste[2][1] = chr(plaque_liste[2][1])

plaque_liste[0], plaque_liste[2] = ("").join(plaque_liste[0]),
("").join(plaque_liste[2])
plaque_liste[1] = str(plaque_liste[1])
if (len(plaque_liste[1]) == 1):
    plaque_liste[1] = "00" + plaque_liste[1]
elif (len(plaque_liste[1]) == 2):
    plaque_liste[1] = "0" + plaque_liste[1]

print("-".join(plaque_liste))
