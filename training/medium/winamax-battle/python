from collections import deque

cards1 = deque([raw_input() for _ in range(int(input()))])
cards2 = deque([raw_input() for _ in range(int(input()))])

order = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

rnd = 0
while len(cards1) > 0 and len(cards2) > 0:
    rnd += 1
    c1, c2 = cards1.popleft(), cards2.popleft()
    heap1, heap2 = [c1], [c2]
    
    v1, v2 = order.index(c1[:-1]), order.index(c2[:-1])
    
    while v1 == v2:
        if len(cards1) > 3 and len(cards2) > 3:
            [heap1.append(cards1.popleft()) for _ in range(3)]
            [heap2.append(cards2.popleft()) for _ in range(3)]
        else:
            print "PAT"
            break
            
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
    winner = (len(cards2) > 0) + 1
    print winner, rnd
