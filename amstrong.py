n=int(input())
s=0
t=n
while t>0:
	d=t%10
	s=s+d*d*d
	t=t//10
if s==n:
	print("yes")
else:
	print("no")
