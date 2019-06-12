
n, m, c = [int(i) for i in raw_input().split()]
consumption = [[int(i), False] for i in raw_input().split()]
toggle = [int(i)-1 for i in raw_input().split()]

consumed = 0
max_consumed = 0
for switch in toggle:
    if not consumption[switch][1]:
        consumed += consumption[switch][0]
        consumption[switch][1] = not consumption[switch][1]
        max_consumed = max(max_consumed, consumed)
    elif consumption[switch][1]:
        consumed -= consumption[switch][0]
        consumption[switch][1] = not consumption[switch][1]
    
    if consumed > c:
        print "Fuse was blown."
        break

else:
    print "Fuse was not blown."
    print "Maximal consumed current was {} A.".format(max_consumed)
