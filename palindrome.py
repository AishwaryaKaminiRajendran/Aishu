N=int(input())
t=N
r=0
while N>0:
	d=N%10
	r=r*10+d
	N=N//10
if (r==t):
	print("yes")
else:
	print("no")
