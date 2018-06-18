dico = {}

nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones,
nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
for i in range(nb_elevators):
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    dico[elevator_floor] = elevator_pos

while True:
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)

    try:
        valeur = dico[clone_floor]
    except:
        valeur = exit_pos

    if clone_pos < valeur and direction == "LEFT":
        instruction = "BLOCK"
    elif clone_pos > valeur and direction == "RIGHT":
        instruction = "BLOCK"
    else:
        instruction = "WAIT"

    print(instruction)
