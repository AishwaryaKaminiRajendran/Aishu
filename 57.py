n,k=map(int,input().split())
a=[int(i) for i in input().split()]
c=0
for j in range(0,len(a)):
	if a[j]==k:
		c=c+1
print(c)
