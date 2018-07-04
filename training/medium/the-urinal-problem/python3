n, libre = int(input()), input().split("!")

longest = list(max(libre, key=len))
idx = libre.index(max(libre, key=len))

if idx == 0:
    longest[0] = "#"
elif idx == len(libre) - 1:
    longest[-1] = "#"
else:
    longest[int((len(longest) - 1) / 2)] = "#"

libre[libre.index(max(libre, key=len))] = "".join(longest)

print("!".join(libre).index("#"))
