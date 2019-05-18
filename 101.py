a,b=map(str,input().split())

c=int(b)

d=a[::-1]
e=[]
for i in range(0,c):
    e.append(d[i])
f=e[::-1]

for j in range(0,len(f)):
    print(f[j],end="")
