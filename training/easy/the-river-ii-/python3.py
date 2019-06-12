r1 = int(input())
r2 = r1 - 1

def next_number(nb):
    chiffres = [int(ch) for ch in str(nb)]
    return nb + sum(chiffres)

while r2 > 0:
    if next_number(r2) == r1:
        print("YES")
        break
    r2 -= 1
else:
    print("NO")
