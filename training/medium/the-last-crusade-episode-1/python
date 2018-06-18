import sys
import math

w, h = [int(i) for i in raw_input().split()]
terrain = [raw_input().split(" ") for i in range(h)]
ex = int(raw_input())  # the coordinate along the X axis of the exit (not
useful for this first mission, but must be read).

while True:
    xi, yi, pos = raw_input().split()
    xi = int(xi)
    yi = int(yi)

    x, y = xi, yi

    if terrain[y][x] == "1" or terrain[y][x] == "3" or terrain[y][x] == "7" or
terrain[y][x] == "8" or terrain[y][x] == "9" or terrain[y][x] == "12" or
terrain[y][x] == "13":
        y += 1
    elif pos == "TOP" and (terrain[y][x] == "4" or terrain[y][x] == "10"):
        x -= 1
    elif pos == "TOP" and (terrain[y][x] == "5" or terrain[y][x] == "11"):
        x += 1
    elif pos == "LEFT" and (terrain[y][x] == "2" or terrain[y][x] == "6"):
        x += 1
    elif pos == "LEFT" and (terrain[y][x] == "5"):
        y += 1
    elif pos == "RIGHT" and (terrain[y][x] == "2" or terrain[y][x] == "6"):
        x -= 1
    elif pos == "RIGHT" and (terrain [y][x] == "4"):
        y += 1

    print(str(x) + " " + str(y))
