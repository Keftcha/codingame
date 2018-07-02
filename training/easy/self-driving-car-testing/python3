n = int(input())
position, *instructions = input().split(";")
position = int(position) - 1    # Because he start to count at 1
route = []

for i in range(n):
    nb, paterne = input().split(";")
    route.append([int(nb), list(paterne)])

while len(route) > 0 and len(instructions) > 0:
    
    # Get the road pattern
    portion = [elem for elem in route[0][1]]
    route[0][0] -= 1
    if route[0][0] == 0:
        del route[0]
    
    # Get the direction
    instruction = instructions[0]
    nombre, direction = int(instruction[:-1]), instruction[-1]
    # Change the direction
    nombre -= 1
    if direction == "L":
        position -= 1
    elif direction == "R":
        position += 1
    if nombre == 0:
        del instructions[0]
    else:
        instructions[0] = str(nombre) + direction
    
    # Place the car
    portion[position] = "#"
    
    print("".join(portion))
