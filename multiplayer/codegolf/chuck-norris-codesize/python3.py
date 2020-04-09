r=lambda l:"{:07b}".format(ord(l))
m="".join(map(r,list(input())))
p=""
o=""
for e in m:
 if e!=p:o+=(" 00 "," 0 ")[int(e)];p=e
 o+="0"
print(o[1:])
