grid = []
for _ in range(9):
    grid.append(raw_input().split())

possibilities = []
frmt = lambda x, y: "{} {}".format(x, y)
add = lambda liste, liste_elem: liste.append(" ".join(sorted(liste_elem)))

for y, line in enumerate(grid):
    for x, nb in enumerate(line):
        # the two tokens at our left are the same
        if  x >= 2 and line[x-2] == line[x-1]:
            # we look for an other same token around us
            if y >= 1 and grid[y][x-1] == grid[y-1][x]:    # the token is on our top
                add(possibilities, (frmt(y, x), frmt(y-1, x)))
            if x < 8 and grid[y][x-1] == grid[y][x+1]:    # the token is on our right
                add(possibilities, (frmt(y, x), frmt(y, x+1)))
            if y < 8 and grid[y][x-1] == grid[y+1][x]:    # the token is on out bottom
                add(possibilities, (frmt(y, x), frmt(y+1, x)))
        
        # the two tokens after us are the same
        if x < 7 and line[x+1] == line[x+2]:
            if y >= 1 and grid[y][x+1] == grid[y-1][x]:    # the token is on out top
                add(possibilities, (frmt(y, x), frmt(y-1, x)))
            if x > 0 and grid[y][x+1] == grid[y][x-1]:    # the token is on our left
                add(possibilities, (frmt(y, x), frmt(y, x-1)))
            if y < 8 and grid[y][x+1] == grid[y+1][x]:    # the token is on out bottom
                add(possibilities, (frmt(y, x), frmt(y+1, x)))
        
        # the token at left is the same as the one at right
        if x > 0 and x < 8 and line[x-1] == line[x+1]:
            if y > 0 and grid[y][x-1] == grid[y-1][x]:    # the token is on our top
                add(possibilities, (frmt(y, x), frmt(y-1, x)))
            if y < 8 and grid[y][x-1] == grid[y+1][x]:    # the token is on out bottom
                add(possibilities, (frmt(y, x), frmt(y+1, x)))
        
        
        # the two tokens at our top are the same
        if y >= 2 and grid[y-2][x] == grid[y-1][x]:
            if x > 0 and grid[y-1][x] == grid[y][x-1]:    # the token is on our left
                add(possibilities, (frmt(y, x), frmt(y, x-1)))
            if y < 8 and grid[y-1][x] == grid[y+1][x]:    # the token is on our bottom
                add(possibilities, (frmt(y, x), frmt(y+1, x)))
            if x < 8 and grid[y-1][x] == grid[y][x+1]:    # the token is on our right
                add(possibilities, (frmt(y, x), frmt(y, x+1)))
        
        # the two tokens at out bottom are the same
        if y < 7 and grid[y+1][x] == grid[y+2][x]:
            if x > 0 and grid[y+1][x] == grid[y][x-1]:    # the token is on our left
                add(possibilities, (frmt(y, x), frmt(y, x-1)))
            if y > 0 and grid[y+1][x] == grid[y-1][x]:    # the token is on our top
                add(possibilities, (frmt(y, x), frmt(y-1, x)))
            if x < 8 and grid[y+1][x] == grid[y][x+1]:    # the token is on out right
                add(possibilities, (frmt(y, x), frmt(y, x+1)))
        
        # the token at top is the same as the one at bottom
        if y > 0 and y < 8 and grid[y-1][x] == grid[y+1][x]:
            if x > 0 and grid[y-1][x] == grid[y][x-1]:    # the token is on our left
                add(possibilities, (frmt(y, x), frmt(y, x-1)))
            if x < 8 and grid[y-1][x] == grid[y][x+1]:    # the token is on our right
                add(possibilities, (frmt(y, x), frmt(y, x+1)))


possibilities = set(possibilities)
print(len(possibilities))
for possibility in sorted(possibilities):
    print possibility
