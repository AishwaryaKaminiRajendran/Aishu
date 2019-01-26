n=int(input())
i=0
p=1
while n>0:
	d=n%10
	p=p*d
	n=n//10
print(p)
