x, y = input(), input()

letters = {}
for idx in range(len(x)):
    if x[idx] in letters.keys() and letters[x[idx]] != y[idx]:
        print("CAN'T")
        break
    else:
        letters[x[idx]] = y[idx]
else:
    letters = [key + "->" + value if key != value else None for key, value in letters.items()]
    # None is evaluate to false
    # if we have at leaste one not None element, that mean we have letters convertion
    if not any(letters):
        print("NONE")
    else:
        [print(elem) for elem in letters if elem]
