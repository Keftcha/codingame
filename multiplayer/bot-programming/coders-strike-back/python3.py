import sys
import math

boost = True

x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
opponent_x, opponent_y = [int(i) for i in input().split()]
old_poss = (x, y)

# game loop
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    #x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    #opponent_x, opponent_y = [int(i) for i in input().split()]
    current_pos = (x, y)
    
    move = (current_pos[0] - old_poss[0], current_pos[1] - old_poss[1])
    target = (next_checkpoint_x - (move[0] * 3), next_checkpoint_y - (move[1] * 3))
    
    # go slow when we aren't in the good direction
    speed = (-9/4) * abs(next_checkpoint_angle) + 605/2
    
    # go slow when we are near a checkpoint
    if next_checkpoint_dist > 1000 and next_checkpoint_dist < 3000:
        speed /= 5
        
    # speed must be between 0 and 100
    if speed > 100:
        speed = 100
    elif speed < 0:
        speed = 0
    
    # may we can use the boost ?
    if (boost and
        next_checkpoint_dist > 5000 and
        abs(next_checkpoint_angle) < 20
    ):
        speed = "BOOST"
        boost = False
    else:
        speed = str(int(speed))
        
    print(str(target[0]) + " " + str(target[1]) + " " + speed)
    #print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + speed)
    
    old_poss = (x, y)
    
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]
    
