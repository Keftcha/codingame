import sys

def can_pass(speed, light):
    speed /= 3.6    # convert the speed in km/h in m/s
    # the number of time the light change his colour
    idx = 0
    while True:
        if idx == 0:
            # the speed for pass before the light turn red for the forst time
            lowest_speed = light[0] / (light[1] * (idx + 1))
            if speed > lowest_speed:
                return True
        else:
            # the speed for pass the light just after it pass green
            highest_speed = light[0] / (light[1] * idx)
            # the speed for pass before the light turn red the idx + 1 time
            lowest_speed = light[0] / (light[1] * (idx + 1))
            
            if highest_speed >= speed > lowest_speed:
                return True
            elif highest_speed < speed:
                return False
        # increment 2 because une time the light is red and after it is green
        # we want to calculate when the light is green
        idx += 2


max_speed = int(input())
print(max_speed, file=sys.stderr)

light_count = int(input())
lights = []
for i in range(light_count):
    distance, duration = [int(j) for j in input().split()]
    lights.append((distance, duration))
    
print(lights, file=sys.stderr)

while max_speed > 0:
    if all([can_pass(max_speed, light) for light in lights]):
        print(max_speed)
        break
    max_speed -= 1
