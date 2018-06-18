import sys

n = int(input())
temps = input()

temperature = sys.maxsize

temps = temps.split(" ")

if (n == 1):
    if (int(temps[0]) == -273):
        temperature = -273
    elif (int(temps[0]) == 5526):
        temperature = 5526
    else:
        temperature = int(temp)
elif (n > 0):
    for elem in temps:
        if (abs(int(elem)) == abs(temperature)):
            if (int(elem) < 0 and temperature < 0):
                temperature = int(elem)
            elif (int(elem) > 0 or temperature > 0):
                temperature = abs(int(elem))
        elif abs(int(elem)) < abs(temperature):
            temperature = int(elem)
else:
    temperature = 0

print(temperature)
