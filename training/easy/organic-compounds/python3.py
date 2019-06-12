n = int(input())
molecule = []
for i in range(n):
    compound = input()
    line = []
    for idx in range(0, len(compound), 3):
        elem = compound[idx:idx+3]
        if "CH" in elem:
            line.append(("a", int(elem[-1])))    # a pour atom
        elif "(" in elem:
            line.append(("l", int(elem[1])))    # l pour liaison
        else:
            line.append(("n", 0))    # n pour None
    molecule.append(line)

valid_eh = True

for idx, line in enumerate(molecule):
    for index, elem in enumerate(line):
        if elem[0] == "a":
            electrons = elem[1]
            x, y = [-1, 1], [-1, 1]
            
            if idx == 0 or len(molecule[idx - 1]) < index:
                y.pop(y.index(-1))
            if idx == len(molecule) -1 or len(molecule[idx + 1]) < index:
                y.pop(y.index(1))
                
            if index == 0:
                x.pop(x.index(-1))
            if index == len(line) -1:
                x.pop(x.index(1))
            
            for elem in y:
                electrons += molecule[idx + elem][index][1]
            for elem in x:
                electrons += molecule[idx][index + elem][1]
                
            if electrons != 4:
                valid_eh = False
                break
            
    if not valid_eh:
        break

print("VALID" if valid_eh else "INVALID")
