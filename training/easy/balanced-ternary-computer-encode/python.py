number = int(raw_input())
tenary = []

exponent = 0
while number != 0:# and number != 3 ** exponent:
    digit = (number % 3 ** (exponent + 1)) / 3 ** exponent
    if digit == 2:
        digit = -1
        caractere = "T"
    else:
        caractere = str(int(digit))
    tenary.append(caractere)
    
    number -= digit * 3 ** exponent
    exponent += 1
    
if number == 3 ** exponent:
    tenary.append(str(1))

tenary.reverse()
print("".join(tenary) or "0")
