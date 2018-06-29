crochet = 0
acolade = 0
parenthese = 0

for elem in input():
    if elem == "{":
        acolade += 1
    elif elem == "[":
        crochet += 1
    elif elem == "(":
        parenthese += 1
    elif elem == "}":
        acolade -= 1
    elif elem == "]":
        crochet -= 1
    elif elem == ")":
        parenthese -= 1

    if (
        crochet < 0 or
        acolade < 0 or
        parenthese < 0
    ):
        break

print("true") if (crochet == 0 and acolade == 0 and parenthese == 0) else print("false")
