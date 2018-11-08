corners = []
for i in range(int(input())):
    x, y = [int(j) for j in raw_input().split()]
    corners.append((x, y))

shoots = []
for i in range(int(input())):
    x, y = [int(j) for j in raw_input().split()]
    shoots.append((x, y))


for shoot in shoots:
    idx = 0
    while idx < len(corners):
        c1, c2 = corners[idx], corners[(idx+1)%len(corners)]
        
        v_ref = (c2[0] - c1[0], c2[1] - c1[1])
        vs = (shoot[0] - c1[0], shoot[1] - c1[1])
        
        determinant = v_ref[0] * vs[1] - v_ref[1] * vs[0]
        
        idx += 1
        
        if determinant >= 0:
            continue
        else:
            print("miss")
            break
        
    else:
        print("hit")
        
