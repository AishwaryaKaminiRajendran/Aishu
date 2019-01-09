N,K=map(int,input().split())
x=[int(i) for i in input().split()]
if N>=K:
	s=[]
	for i in range (0,K):
		s.append(x[i])
	print(sum(s))
 

