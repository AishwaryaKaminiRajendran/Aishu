N=int(input())
i=1
while i<=N:
	if N%i==0:
		c=c+1
if c==2:
	print("yes")
else:
	print("no")
