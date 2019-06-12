input()
l=[int(i)for i in raw_input().split()]
print(l and sorted(sorted(l,reverse=1),key=abs)[0]or 0)
