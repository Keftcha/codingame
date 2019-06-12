import sys

horses = []
for i in range(int(input())):
    horses.append(tuple([int(j) for j in input().split()]))

force = sys.maxsize
for idx, horse in enumerate(horses):
    for opponent in horses[idx + 1:]:
        if abs(horse[0] - opponent[0]) + abs(horse[1] - opponent[1]) < force:
            force = abs(horse[0] - opponent[0]) + abs(horse[1] - opponent[1])

print(force)
