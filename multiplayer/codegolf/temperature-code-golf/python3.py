input()
l=[int(i)for i in input().split()]
l.sort(reverse=1)
l.sort(key=abs)
print(l and l[0]or 0)