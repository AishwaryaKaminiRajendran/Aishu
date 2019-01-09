N=int(input())
a=[]
for i in range(0,N):
	x=map(int,input().split())
	a.append(x)
print(a)
print(max(a))
