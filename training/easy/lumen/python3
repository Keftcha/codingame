def lighting(light_pos, power, alight):
    for y in range(-power+1,power):
        for x in range(-power+1,power):
            if (
                0 <= light_pos[1] + y < len(alight) and
                0 <= light_pos[0] + x < len(alight[y])
            ):
                alight[light_pos[1] + y][light_pos[0] + x] = "¤"

n, l = int(input()), int(input())

field = [input().split() for i in range(n)]
lighted = [list("0" * n) for _ in range(n)]

for y, line in enumerate(field):
    for x, elem in enumerate(line):
        if elem == "C":
            lighting((x, y), l, lighted)

print(sum([line.count("0") for line in lighted]))
