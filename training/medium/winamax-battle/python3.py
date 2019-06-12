from collections import deque

# cards players have in their heap
cards1 = deque([input() for _ in range(int(input()))])
cards2 = deque([input() for _ in range(int(input()))])

order = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

rnd = 0    # number of round played
while len(cards1) > 0 and len(cards2) > 0:
    rnd += 1
    # card that the player poses
    c1, c2 = cards1.popleft(), cards2.popleft()
    # heap of players on the table
    heap1, heap2 = [c1], [c2]
    
    # value of cards
    v1, v2 = order.index(c1[:-1]), order.index(c2[:-1])
    
    # compare cards
    while v1 == v2:    # bataille
        # discard 3 cards only if there is enouth cards
        if len(cards1) > 3 and len(cards2) > 3:
            [heap1.append(cards1.popleft()) for _ in range(3)]
            [heap2.append(cards2.popleft()) for _ in range(3)]
        else:
            print("PAT")
            break
            
        # the card players pose
        c1, c2 = cards1.popleft(), cards2.popleft()
        heap1.append(c1)
        heap2.append(c2)
        v1, v2 = order.index(c1[:-1]), order.index(c2[:-1])
        
    else:
        if v1 > v2:
            cards1.extend(heap1 + heap2)
        elif v2 > v1:
            cards2.extend(heap1 + heap2)
        continue

    break

else:
    winner = (len(cards2) > 0) + 1    # define who is the winner
    print(winner, rnd)
