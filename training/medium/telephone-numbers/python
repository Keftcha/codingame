def add_number(tree, number, idx):
    add = 0
    for neud in tree[1]:
        # we already got the number 
        if idx < len(number) and neud[0] == number[idx]:
            add += add_number(neud, number, idx+1)
            break
    else:
        if idx < len(number):
            # neud isn't find in the tree
            add += 1
            tree[1].append((number[idx], []))
            if idx < len(number)-1:
                add += add_number(tree[1][-1], number, idx + 1)
    return add
        
        
n = int(input())
tree = ("#", [])
nb = 0
for i in range(n):
    telephone = raw_input()
    nb += add_number(tree, telephone, 0)

print nb
