min_nb, max_nb = 0, 100

for i in range(int(input())):
    line = input().split(" ")
    line[0] = int(line[0])
    
    if line[-1] == "high" and line[0] < max_nb:
        max_nb = line[0]
    elif line[-1] == "low" and line[0] > min_nb:
        min_nb = line[0]
    
    if (
        (max_nb - min_nb <= 1) or
        (line[0] > max_nb and line[-1] != "high") or
        (line[0] < min_nb and line[-1] != "low")
    ):
        print("Alice cheated in round {}".format(i + 1))
        break
    
else:
    print("No evidence of cheating")
