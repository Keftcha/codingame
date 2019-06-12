x, y = raw_input(), raw_input()

keys, values = [], []
for idx in range(len(x)):
    if x[idx] in keys and values[keys.index(x[idx])] != y[idx]:
        print("CAN'T")
        break
    elif not x[idx] in keys:
        keys.append(x[idx])
        values.append(y[idx])
else:
    correspondance = []
    for idx in range(len(keys)):
        key, value = keys[idx], values[idx]
        if key != value:
            correspondance.append(key + "->" + value)
    if not correspondance:
        print("NONE")
    else:
        for elem in correspondance:
            if elem:
                print elem
