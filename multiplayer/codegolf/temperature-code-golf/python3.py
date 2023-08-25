input()
print(min(input().split() or "0", key=lambda n: abs(int(n) - 0.1)))
