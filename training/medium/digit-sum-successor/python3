import sys

def to_list(number):
    return [int(digit) for digit in str(number)]


def to_number(liste):
    return int("".join([str(digit) for digit in liste]))


n = to_list(int(input()))
print(n, file=sys.stderr)

idx = len(n) - 1
# get the index of the last digit 
while n[idx] == 0:
    idx -= 1

# remove one to the lastest digit
n[idx] = n[idx] -1

if idx == 0:
    # if we arrived on the first digit,
    #we have to get a new one in our number
    n.insert(0, 1)
else:
    # add one to the previous digit
    idx -= 1
    n[idx] += 1
    # a digit can't bo higher than 9
    # we check it here
    while n[idx] == 10:
        if idx == 0:
            # may we are on the first digit
            # wa have to add a new one
            n[idx] -= 1
            n.insert(0, 1)
        else:
            # otherwise we reduce the digit to 9 and
            # add 1 to the previous digit
            n[idx] -= 1
            n[idx-1] += 1
            idx -= 1

# sort the n[idx+1:] digit to get the lowest number
# higher than the given number due to the n[:idx+1]
n = n[:idx+1] + sorted(n[idx+1:])
print(to_number(n))
