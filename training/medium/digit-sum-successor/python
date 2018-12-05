def to_list(number):
    return [int(digit) for digit in str(number)]


def to_number(liste):
    return int("".join([str(digit) for digit in liste]))


n = to_list(int(input()))

idx = len(n) - 1
while n[idx] == 0:
    idx -= 1

n[idx] = n[idx] -1

if idx == 0:
    n.insert(0, 1)
else:
    idx -= 1
    n[idx] += 1
    while n[idx] == 10:
        if idx == 0:
            n[idx] -= 1
            n.insert(0, 1)
        else:
            n[idx] -= 1
            n[idx-1] += 1
            idx -= 1

n = n[:idx+1] + sorted(n[idx+1:])
print(to_number(n))
