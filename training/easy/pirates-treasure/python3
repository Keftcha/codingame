input()

carte = []
for i in range(int(input())):
    line = []
    for j in input().split():
        v = int(j)
        line.append(v)
    carte.append(line)

for y, line in enumerate(carte):
    for x, obstacle in enumerate(line):
        if not obstacle:
            deb_y, fin_y = -1, 2
            deb_x, fin_x = -1, 2
            
            # Beware ! don't go out of the map
            if y == 0:
                deb_y = 0
            if y == len(carte) - 1:
                fin_y = 1
            if x == 0:
                deb_x = 0
            if x == len(line) - 1:
                fin_x = 1
            
            # Count obstacles
            nb_obstacle = 0
            for nb_y in range(deb_y, fin_y):
                for nb_x in range(deb_x, fin_x):
                    if carte[y + nb_y][x + nb_x]:
                        nb_obstacle += 1
            
            if deb_y == 0 or fin_y == 1:
                if deb_x == 0 or fin_x == 1:
                    # Here we are in a corner
                    if nb_obstacle == 3:
                        print(x, y)
                elif nb_obstacle == 5:
                    # Here we are on the first or last line
                    print(x, y)
            elif (deb_x == 0 or fin_x == 1) and nb_obstacle == 5:
                # Here we are on the first or last column
                print(x, y)
            elif nb_obstacle == 8:
                # We are in the center of the map
                print(x, y)
