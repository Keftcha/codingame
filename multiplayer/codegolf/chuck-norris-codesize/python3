b="".join(["{:07b}".format(ord(l))for l in input()])
f=lambda d,f,c:("00 "if c=="0"else"0 ")+(f-d)*"0"
c=""
p=0
for i,e in enumerate(b):
 if e!=b[p]:c+=f(p,i,b[p])+" ";p=i
print(c+f(p,i+1,b[p]))
