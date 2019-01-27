a=int(input())
s=0
t=a
while t>0:
	d=t%10
	s=s+d*d*d
	t=t//10
if s==a:
	print("yes")
else:
	print("no")
