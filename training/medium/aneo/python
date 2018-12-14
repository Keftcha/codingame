def can_pass(speed, light):
    speed /= 3.6
    idx = 0
    while True:
        if idx == 0:
            lowest_speed = light[0] / (light[1] * (idx + 1))
            if speed > lowest_speed:
                return True
        else:
            highest_speed = light[0] / (light[1] * idx)
            lowest_speed = light[0] / (light[1] * (idx + 1))
            
            if highest_speed >= speed > lowest_speed:
                return True
            elif highest_speed < speed:
                return False
        idx += 2


max_speed = int(raw_input())

light_count = int(raw_input())
lights = []
for i in range(light_count):
    distance, duration = [float(j) for j in raw_input().split()]
    lights.append((distance, duration))

while max_speed > 0:
    if all([can_pass(max_speed, light) for light in lights]):
        print max_speed
        break
    max_speed -= 1
