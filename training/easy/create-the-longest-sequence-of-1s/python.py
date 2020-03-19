b = input().split("0")

maxOne = 1
idx = 0
while idx+1 < len(b):
    maxOne = max(maxOne, len(b[idx]) + len(b[idx+1]) + 1)
    idx += 1

print(maxOne)
