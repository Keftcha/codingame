tributes = int(raw_input())
names = {}
for i in range(tributes):
    player_name = raw_input()
    names[player_name] = {"killed": [], "killer": None}
    
turns = int(input())
for i in range(turns):
    info = raw_input().split()
    killed = [name.strip(",") for name in info[2:]]
    names[info[0]]["killed"].extend(killed)
    for name in killed:
        names[name.strip(",")]["killer"] = info[0]

idx = 1
for tribue, info in sorted(names.items()):
    print "Name: " + tribue
    print "Killed:", ", ".join(sorted(info["killed"])) if info["killed"] else None
    print "Killer:", "Winner" if info["killer"] == None else info["killer"]
    if idx != tributes:
        print
    idx += 1
