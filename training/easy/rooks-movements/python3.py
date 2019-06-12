rook = tuple(input())
# convert rook place to x y cooddonate
rook = tuple((ord(rook[0]) - 97, int(rook[1]) -1))

x_min = y_min = (0, False)    # idx, True if the rook replace opponent
x_max = y_max = (7, False)

for i in range(int(input())):
    piece = input().split(" ")
    
    # convert piece place to x y coordonate
    piece = tuple((int(piece[0]), (ord(piece[1][0]) - 97, int(piece[1][1]) -1)))    # ord("a") == 97
    
    # is the piece on the same column
    if rook[0] == piece[1][0]:
        # is the piece's line is upper or lower than my rook ?
        if piece[1][1] > rook[1]:
            y_max = (piece[1][1] if piece[0] else piece[1][1] - 1, piece[0])    # we check if the rook can replace an opponent
        elif piece[1][1] < rook[1]:
            y_min = (piece[1][1] if piece[0] else piece[1][1] + 1, piece[0])    # here too
    # is the piece and the rook on the same line ?
    if rook[1] == piece[1][1]:
        # is the piece is before or after my rook ?
        if piece[1][0] > rook[0]:
            x_max = (piece[1][0] if piece[0] else piece[1][0] - 1, piece[0])    # the same
        elif piece[1][0] < rook[0]:
            x_min = (piece[1][0] if piece[0] else piece[1][0] + 1, piece[0])    # again

# Convert rook coordinate to chess place
rook = chr(rook[0] + 97) + str(rook[1] + 1)

possible_places = []
# search all possible place in the column
for idx in range(x_min[0], x_max[0] + 1):
    marqueur = "x" if (idx == x_min[0] and x_min[1]) or (idx == x_max[0] and x_max[1]) else "-"
    place = "R" + rook + marqueur + chr(idx + 97) + rook[1]    # ascii code for "a" is 97
    if place[-2:] != rook:
        possible_places.append(place)
# search all possible place in the line
for idx in range(y_min[0], y_max[0] + 1):
    marqueur = "x" if (idx == y_min[0] and y_min[1]) or (idx == y_max[0] and y_max[1]) else "-"
    place = "R" + rook + marqueur + rook[0] + str(idx + 1)
    if place[-2:] != rook:
        possible_places.append(place)

possible_places.sort()
print("\n".join(possible_places))
