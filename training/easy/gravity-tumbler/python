width, height = [int(i) for i in raw_input().split()]
count = int(raw_input())

things = []
for i in range(height):
    things.append(list(raw_input()))

def rotate(thing):
    second_thing = []
    for idx in range(len(things[0])):
        line = []
        for index in range(len(things)):
            line.append(things[index][idx])
        second_thing.append(line)
    second_thing.reverse()
    return second_thing


def apply_gravity(thing):
    new_thing = []
    for line in thing:
        new_line = "".join(("".join(line)).split("."))
        nb_pts = len(thing[0]) - len(new_line)
        new_line += "." * nb_pts
        new_thing.append(list(new_line))
    return new_thing
    

for _ in range(count):
    things = apply_gravity(things)
    things = rotate(things)

for line in things:
    print("".join(line))
