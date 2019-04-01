w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())
batman = tuple([int(i) for i in raw_input().split()])

x, y = (0, w), (0, h)
while True:
    bomb_dir = raw_input()
    
    if "U" in bomb_dir:
        y = (y[0], batman[1]-1)
    elif "D" in bomb_dir:
        y = (batman[1] + 1, y[1])
    
    if "R" in bomb_dir:
        x = (batman[0] + 1, x[1])
    elif "L" in bomb_dir:
        x = (x[0], batman[0]-1)
    
    bx = x[0] + int((x[1] - x[0])/2)
    by = y[0] + int((y[1] - y[0])/2)
    
    batman = bx, by
    
    print batman[0], batman[1]
