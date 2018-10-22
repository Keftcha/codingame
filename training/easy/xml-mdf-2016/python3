sequence = input()
profondeurs = {}
depth = 0

# get the depth of all tags
idx = 0
while idx < len(sequence):
    char = sequence[idx]
    # change the depth
    if char == "-":
        depth -= 1
        idx += 1
    else:
        depth += 1
        if not char in profondeurs.keys():
            profondeurs[char] = [1 / depth]
        else:
            profondeurs[char].append(1 / depth)
    idx += 1

# calcul the weight of tags by name
for key, value in profondeurs.items():
    profondeurs[key] = sum(value)

print(max(profondeurs, key=profondeurs.get))
