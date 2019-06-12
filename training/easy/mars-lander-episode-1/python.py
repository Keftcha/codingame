surface_n = int(raw_input())
for i in xrange(surface_n):
    land_x, land_y = [int(j) for j in raw_input().split()]

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in
raw_input().split()]

    if (v_speed < -39):
        print("0 4")
    else:
        print("0 0")
