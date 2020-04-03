import sys
import math

def norme(v):
    return math.sqrt(v[0]**2 + v[1]**2)


def vector_angle(v1, v2):
    # si la norme d'un vecteur est 0 alors c'est un poin
    # l'angle entre un point et un vecteur est de 0 radiants
    if norme(v1) == 0 or norme(v2) == 0:
        return 0
    # demonstration du calcul: http://www.jybaudot.fr/Vecteursmatrices/ptscalangles.html
    angle = math.acos(
        (v1[0]*v2[0] + v1[1]*v2[1]) /
        (norme(v1) * norme(v2))
    )
    # resultat en radiant
    return angle


class Module(object):
    def __init__(self):
        self.boost = True
    
    def move(self, x, y, vx, vy, angle, next_check_point_id, checkpoints):
        pos = (x, y)
        speed = (vx, vy)
        ncp = checkpoints[next_check_point_id]
        to_ncp = (ncp[0] - pos[0], ncp[1] - pos[1])
        ncp_angle = vector_angle(speed, to_ncp)
        ncp_dist = norme(to_ncp)
        target = (ncp[0] - speed[0] * 3, ncp[1] - speed[1] * 3)
        
        # go slow when we aren't in the good direction
        power = (-90/(math.cos((13*math.pi)/18))) * math.cos(ncp_angle) + 100
        
         # go slow when we are near a checkpoint
        if ncp_dist > 1000 and ncp_dist < 2000 and power > 50:
            power /= 5
            
        # speed must be between 0 and 100
        if power > 100:
            power = 100
        elif power < 10:
            power = 10
        
        # may we can use the boost ?
        if (self.boost and
            ncp_dist > 5000 and
            math.cos(ncp_angle) > math.cos(math.radians(20)) # le boost fait un peu nawak non? c'est peut-être a cause de l'angle je pense
        ):
            power = "BOOST"
            self.boost = False
        else:
            power = str(round(power))
        # il y a vraimnt un gros soucis avec le boost
        
        print("pos", pos, file=sys.stderr)
        print("speed", speed, file=sys.stderr)
        print("ncp", ncp, file=sys.stderr)
        print("ncp_angle", ncp_angle, file=sys.stderr)
        print("cos(ncp_angle)", math.cos(ncp_angle), file=sys.stderr)
        print("ncp_dist", ncp_dist, file=sys.stderr)
        print("target", target, file=sys.stderr)
        print(file=sys.stderr)
        
        return str(target[0]) + " " + str(target[1]) + " " + power
        

laps = int(input())
checkpoint_count = int(input())
checkpoints = []
for i in range(checkpoint_count):
    checkpoint_x, checkpoint_y = [int(j) for j in input().split()]
    checkpoints.append((checkpoint_x, checkpoint_y))

modules = (Module(), Module())

# game loop
while True:
    for i in range(2):
        # x: x position of your pod
        # y: y position of your pod
        # vx: x speed of your pod
        # vy: y speed of your pod
        # angle: angle of your pod
        # next_check_point_id: next check point id of your pod
        x, y, vx, vy, angle, next_check_point_id = [int(j) for j in input().split()]
        print(modules[i].move(x, y, vx, vy, angle, next_check_point_id, checkpoints))
        
        
    for i in range(2):
        # x_2: x position of the opponent's pod
        # y_2: y position of the opponent's pod
        # vx_2: x speed of the opponent's pod
        # vy_2: y speed of the opponent's pod
        # angle_2: angle of the opponent's pod
        # next_check_point_id_2: next check point id of the opponent's pod
        x_2, y_2, vx_2, vy_2, angle_2, next_check_point_id_2 = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # You have to output the target position
    # followed by the power (0 <= thrust <= 100)
    # i.e.: "x y thrust"
