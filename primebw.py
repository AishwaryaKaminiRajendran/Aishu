a,b=map(int,input().split())
j=a
for i in range (1,a):
	while j<=b:
		if j%i==0:
			print(j)
		j=j+1

		
		
