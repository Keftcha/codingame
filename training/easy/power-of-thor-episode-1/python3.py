import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
idx_x, idx_y = 0, 0

while True:
    remaining_turns = int(input())
    direction = []
    deplacement_x = abs(light_x - initial_tx)
    deplacement_y = abs(light_y - initial_ty)

    if (idx_y < deplacement_y):
        if (initial_ty < light_y):
            direction.append("S")
        if (initial_ty > light_y):
            direction.append("N")
        idx_y += 1

    if (idx_x < deplacement_x):
        if (initial_tx < light_x):
            direction.append("E")
        if (initial_tx > light_x):
            direction.append("W")
        idx_x += 1

    print("".join(direction))
