import math

def norme(v):
    return math.sqrt(v[0]**2 + v[1]**2)


def orthogonaux(v1, v2):
    # two vector are orthogonaux if their scale product is equal to 0
    
    return v1[0] * v2[0] + v1[1] * v2[1] == 0


def form_vector(form):     # a form is a list of 4 points
    """ Function who take four point of a form and
    return the four vectors of the four side of the form """
    
    a, b, c, d = form
    
    vab = (b[0] - a[0], b[1] - a[1])    # vector ab
    vbc = (c[0] - b[0], c[1] - b[1])    # vector bc
    vcd = (d[0] - c[0], d[1] - c[1])    # opposite vector of ab, the vector cd
    vda = (a[0] - d[0], a[1] - d[1])    # opposite vector of bc, the vector da
    
    return (vab, vbc, vcd, vda)
    
    
def colinear(v1, v2):
    # check if x of the vectors aren't 0
    if v1[0] == 0 or v2[0] == 0:
        rapport_x = 0
    else:
        rapport_x = v1[0]/v2[0]
    # check if y of the vectors aren't 0
    if v1[1] == 0 or v2[1] == 0:
        rapport_y = 0
    else:
        rapport_y = v1[1]/v2[1]
    
    return rapport_x == rapport_y


def parallelogram(sides):    # the four side of a form
    vab, vbc, vcd, vda = sides

    # a form is a parallelograp if their vector are colinear two by two
    return colinear(vab, vcd) and colinear(vbc, vda)


def rhombus(sides):
    vab, vbc, vcd, vda = sides
    
    # a form is a thombus if his four side have the same length
    return norme(vab) == norme(vcd) == norme(vbc) == norme(vda)
    

def rectangle(sides):
    vab, vbc, vcd, vda = sides
    
    # a form is a rectangle if each side vector are orthogonaux
    return (
        orthogonaux(vab, vbc) and    # vector ab and bc are orthogonaux
        orthogonaux(vbc, vcd) and    # vector bc and cd
        orthogonaux(vcd, vda) and    # cd and da
        orthogonaux(vda, vab)    # da, ab
    )


def square(sides):
    return rectangle(sides) and rhombus(sides)


quadrilaterals = []
n = int(input())
for i in range(n):
    a, xa, ya, b, xb, yb, c, xc, yc, d, xd, yd = input().split()
    
    # convert coordinates in int
    xa, ya = int(xa), int(ya)
    xb, yb = int(xb), int(yb)
    xc, yc = int(xc), int(yc)
    xd, yd = int(xd), int(yd)
    
    quadri = {
        a: (xa, ya),
        b: (xb, yb),
        c: (xc, yc),
        d: (xd, yd)
    }
    
    quadrilaterals.append(quadri)
    

for q in quadrilaterals:
    lettres = "".join(q.keys())
    points = list(q.values())
    vectors = form_vector(points)
    
    if square(vectors):
        nature = "square"
    elif rectangle(vectors):
        nature = "rectangle"
    elif rhombus(vectors):
        nature = "rhombus"
    elif parallelogram(vectors):
        nature = "parallelogram"
    else:
        nature = "quadrilateral"

    print("{} is a {}.".format(lettres, nature))
