import math

def calculate_score(liste, player_score):
    player_score_before_round = player_score
    if liste.count("X") == 3:
        return 0
    for idx, elem in enumerate(liste):
        if "*" in elem:
            elem = elem.split("*")
            shoot = int(elem[0]) * int(elem[1])
            
        elif elem == "X":
            if idx != 0 and liste[idx-1] == "X":
                shoot = -30
            else:
                shoot = -20            
        else:
            shoot = int(elem)
        
        player_score += shoot
    
    return player_score


n = int(input())
scores = [0] * n
players = [input() for i in range(n)]
shoots = [input().split() for i in range(n)]


# regroupe shoots by 3
for idx, player_shoot in enumerate(shoots):
    new_player_shoot = []
    index = 0
    while index < len(player_shoot):
        new_player_shoot.append(player_shoot[index:index+3])
        index += 3
    shoots[idx] = new_player_shoot

# calcul points of each player and determine who is the winner
winner = None
turn = 0
while turn < len(max(shoots, key=len)):
    for player_idx, player in enumerate(shoots):
        if len(player) > turn:
            scores[player_idx] = calculate_score(player[turn], scores[player_idx])
            if scores[player_idx] == 101:
                winner = players[player_idx]
                break
    turn += 1
    if winner != None:
        break

if winner == None:
    print(players[scores.index(max(scores))])
else:
    print(winner)
