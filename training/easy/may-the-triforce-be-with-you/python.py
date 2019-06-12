n = int(input())
taille = 2 * n - 1

triangle = [" "*((taille - nb)//2) + "*"*nb for nb in range(1, n*2, 2)]
triangle_spaces = [triangle[idx] + " "*((taille - nb)//2) for idx, nb in enumerate(range(1, n*2, 2))]

# the triangle on the top
t1 = [" "*(taille//2) + line for line in triangle]
# the two triangle on the bottom
t23 = [triangle_spaces[idx] + " " + triangle[idx] for idx in range(n)]

for idx, line in enumerate(t1):
    print (" " if idx > 0 else ".") + line # put the point on the first line

for line in t23:
    print line
