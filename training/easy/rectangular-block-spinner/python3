def square_to_dimond(liste, size):
    liste = [line.split() for line in liste]
    new = []
    x = len(liste[0]) - 1
    y = 0
    
    # the upper half and middle line
    while x >= 0:
        line = []
        tx, ty = x, y
        while tx < len(liste[0]):
            line.append(liste[ty][tx])
            tx += 1
            ty += 1
        new.append(line)
        x -= 1
        
    # the lower half
    y += 1
    while y < len(liste):
        line = []
        tx, ty = x+1, y
        while ty < len(liste):
            line.append(liste[ty][tx])
            tx += 1
            ty += 1
        new.append(line)
        y+= 1
    
    new = [" ".join(line) for line in new]
    
    for idx, line in enumerate(new):
        nb_spaces = int((len(" ".join(liste[0])) - len(line))/2)
        new[idx] = " "*nb_spaces + "".join(line) + " "*nb_spaces
    return new


def dimond_to_square(liste, size):
    liste = [elem.split() for elem in liste]
    
    idx = size
    spaces = 1
    while idx < len(liste):
        liste[idx][:0] = [" "]*spaces
        spaces += 1
        idx += 1
    
    new = []
    x = y = 0
    while y < size:
        tx, ty = x, y
        line = []
        idx = 0
        while idx < size:
            line.append(liste[ty][tx])
            ty += 1
            tx += 1
            idx += 1
        new.append(line)
        y += 1
    
    return [" ".join(elem) for elem in new]
            

size = int(input())
angle = int(input())
#print("angle: ", angle, file=sys.stderr)

form = []
for i in range(size):
    line = input()
    form.append(line)

#[print("".join(line), file=sys.stderr) for line in form]
#print(file=sys.stderr)

functions = (square_to_dimond, dimond_to_square)
idx = 0
while idx * 45 < angle:
    form = functions[idx%2](form, size)
    idx += 1

[print("".join(elem)) for elem in form]
