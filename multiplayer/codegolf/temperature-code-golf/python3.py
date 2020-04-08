input()
print(min(map(int,(input()or"0").split()),key=lambda n:(abs(n-.1))))
