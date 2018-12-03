def hand_round(number):
    number = str(number).split(".")
    return int(number[0]) if int(number[1]) < 5 else int(number[0]) + 1

rounds = int(raw_input())
cash = int(raw_input())

for i in range(rounds):
    # ball result, call by the target, number chose by the the target if the call is "PLAIN"
    play = raw_input().split()
    # convert number to int
    play[0] = int(play[0])
    if len(play) == 3:
        play[2] = int(play[2])
        
    mise = hand_round(cash/4.0)
    cash -= mise
    
    if (
        (play[1] == "EVEN" and play[0]%2 == 0 and play[0] != 0) or
        (play[1] == "ODD" and play[0]%2 == 1)
    ):
        cash += 2 * mise
        
    elif play[1] == "PLAIN" and play[0] == play[2]:
        cash += mise + mise * 35

print cash
