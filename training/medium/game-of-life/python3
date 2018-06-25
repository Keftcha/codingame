def give_live(x, y, cells):
    cells.add((x, y))


def back_to_death(cell, cells):
    nb_cell = 0
    for nb in range(-1, 2):
        for nombre in range(-1, 2):
            if (cell[0] + nombre, cell[1] + nb) in cells:
                nb_cell += 1
    return nb_cell == 3


def cell_stay_alive(cell, cells, new_cells):
    nb_cell = 0
    for nb in range(-1, 2):
        for nombre in range(-1, 2):
            if (cell[0] + nombre, cell[1] + nb) in cells:
                nb_cell += 1
            elif back_to_death((cell[0] + nombre, cell[1] + nb), cells):
                new_cells.add((cell[0] + nombre, cell[1] + nb))
    return (nb_cell == 3 or nb_cell == 4)


def next_turn(cells):
    new_cells = set()
    for cell in cells:
        if cell_stay_alive(cell, cells, new_cells):
            new_cells.add(cell)
    return new_cells


cells = set()

width, height = [int(i) for i in input().split()]
for idx in range(height):
    line = input()
    for index, elem in enumerate(line):
        if elem == "1":
            give_live(index, idx, cells)

new_cells = next_turn(cells)

for y in range(height):
    for x in range(width):
        if (x, y) in new_cells:
            print("1", end="")
        else:
            print("0", end="")
    print()
