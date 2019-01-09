N=int(input())
s=0
t=N
while N>=0:
	d=N%10
	s=s+d*d*d
	N=N//10
if s==t:
	print("yes")
else:
	print("no")
