r1, r2 = int(raw_input()), int(raw_input())

def next_number(nb):
    chiffres = [int(ch) for ch in str(nb)]
    return nb + sum(chiffres)

while r1 != r2:
    if r1 < r2:
        r1 = next_number(r1)
    elif r1 > r2:
        r2 = next_number(r2)

print(r1)
