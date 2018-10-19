w, h = [int(i) for i in raw_input().split()]
legs = []
for i in range(h):
    line = list(raw_input())
    legs.append(line)
    
# initialising
pointeurs = legs[0][:]

for line in legs[1:len(legs) - 1]:
    if "-" in line:
        # get indexs before and after one or more "-"
        indexs = []
        idx = 0
        while idx < len(line):
            elem = line[idx]
            if elem == "-":
                trait = 1
                while line[trait + idx] == "-":
                    trait += 1
                indexs.append((idx - 1, idx + trait))
                idx += trait + 1
            else:
                idx += 1
        
        idx = 0
        while idx < len(indexs):
            # exchange caracters
            pointeurs[indexs[idx][0]], pointeurs[indexs[idx][1]] = pointeurs[indexs[idx][1]], pointeurs[indexs[idx][0]]
            idx += 1

# remove all white space
pointeurs = "".join([char for char in pointeurs if char != " "])    # the final place of ceracteres
order = "".join([char for char in legs[0] if char != " "])    # the order to print the caracteres (first line)
finish_line = "".join([char for char in legs[-1] if char != " "])    # the finish line caracteres (last line)

for lettre in order:
    print("{}{}".format(lettre, finish_line[pointeurs.index(lettre)]))
