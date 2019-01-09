N=int(input())
s=0
while N>=0:
	d=N%10
	s=s+d*d*d
	N=N//10
if s==N:
	print("yes")
else:
	print("no")
