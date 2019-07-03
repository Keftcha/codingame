import sys
import math

class Motorcicle(object):
    def __init__(self, name, place, speed):
        self.name = name
        self.place = place
        self.speed = speed
    
    def sort_speed(motorcicles):
        """Sort a list of Motorbicle by their speed"""
        motorcicles.sort(key=lambda moto: moto.speed, reverse=True)
    
    def separate_speed(motorcicles, max_speed):
        """Separate bicycle un two list.
        
        Motors with a speed superior at max_speed, and
        motors with a speed inferior or equal to the max speed."""
        
        above, below = [], []
        for moto in motorcicles:
            if moto.speed > max_speed:
                above.append(moto)
            else: # moto.speed <= max_speed
                below.append(moto)
        
        return (above, below)
    
    def __str__(self):
        return (
            "name: " + self.name +
            "\nplace: " + str(self.place) + 
            "\nspeed: " + str(self.speed)
        )
    

def max_speed(turn):
    return math.sqrt(math.tan(math.radians(60)) * (turn * 9.81))
    
    
n = int(input())
v = int(input())
max_speed_circuit = sys.maxsize    # the maximum constant speed of the circuit without fall
motos = []

# create motos
for i in range(n):
    speed = int(input())
    motos.append(Motorcicle(chr(i + 97), 0, speed))

Motorcicle.sort_speed(motos)

# put place for each moto
for idx, moto in enumerate(motos):
    moto.place = idx + 1

radius = [int(input()) for i in range(v)]

for turn in radius:
    # the max speed in the turn
    turn_speed = max_speed(turn)
    
    # select the maximum constant speed of the circuit
    max_speed_circuit = min(max_speed_circuit, turn_speed)
    
    # select which bicycle fall
    fallen, standing = Motorcicle.separate_speed(motos, turn_speed)
    motos = standing + fallen

print(math.floor(max_speed_circuit))
print("y")    # My place
[print(moto.name) for moto in motos]
