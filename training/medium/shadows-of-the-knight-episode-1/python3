import sys
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())     # maximum number of turns before game over.
batman = tuple([int(i) for i in input().split()])    # Batman's place

# x and y interval where the bomb can be
# (min, max) with min and max include
x, y = (0, w), (0, h)    # x is the horizontax axe and y the vertical axe
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if "U" in bomb_dir:
        y = (y[0], batman[1]-1)
    elif "D" in bomb_dir:
        y = (batman[1] + 1, y[1])
    
    if "R" in bomb_dir:
        x = (batman[0] + 1, x[1])
    elif "L" in bomb_dir:
        x = (x[0], batman[0]-1)
    
    
    # the location of the next window Batman should jump to.
    bx = x[0] + round((x[1] - x[0])/2)
    by = y[0] + round((y[1] - y[0])/2)
    
    batman = bx, by
    
    print(bomb_dir, file=sys.stderr)
    print(x, y, file=sys.stderr)
    print(batman, file=sys.stderr)
    
    print(batman[0], batman[1])
