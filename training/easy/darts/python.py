import math

def in_square(square, point):
    idx = 0
    while idx < 4:    # square have 4 point
        p1, p2 = square[idx], square[(idx + 1)%4]
        
        v_ref = (p2[0] - p1[0], p2[1] - p1[1])
        v_dart = (point[0] - p1[0], point[1] - p1[1])
        
        det = v_ref[0] * v_dart[1] - v_ref[1] * v_dart[0]
        
        idx += 1
        
        if det < 0:
            return False
    else:
        return True


def in_circle(circle, point):
    n_point = math.sqrt(point[0]**2 + point[1]**2)    # norme of the position vector
    return circle[1] >= n_point


def in_diamon(diamon, point):
    # the same of square, the point aren't on the same place
    return in_square(diamon, point)
    

size = int(input())
half = size/2

# define the three geometric shape
square = (
    (-half, half),    # top left
    (-half, -half),    # bottom left
    (half, -half),    # bottom right
    (half, half)    # top right
)

circle = ((0, 0), half)    # center of circle, radius of the circle

diamon = (
    (0, half),    # top
    (-half, 0),    # center left
    (0, -half),    # bottom
    (half, 0)    # center right
)

# get the player names and darths location
names = {}
order = []
for i in range(int(input())):
    name = raw_input()
    names[name] = {"darts": [], "score": 0}
    order.append(name)
    
for i in range(int(input())):
    throw_data = raw_input().split()
    names[throw_data[0]]["darts"].append((int(throw_data[1]), int(throw_data[2])))

# count points
for name in order:
    for dart in names[name]["darts"]:
        if in_square(square, dart):
            if in_circle(circle, dart):
                if in_diamon(diamon, dart):
                    points = 15
                else:
                    points = 10
            else:
                points = 5
            names[name]["score"] += points

# make list wih player name and score
results = []
for name in names:
    results.append((names[name]["score"], name))

# sort plauers by their name
results.sort(key=lambda tup: order.index(tup[1]))
# sort players by theis score
results.sort(reverse=True, key=lambda tup: tup[0])

for score, name in results:
    print("{} {}".format(name, score))
