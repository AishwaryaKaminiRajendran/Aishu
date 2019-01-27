n,k=map(int,input().split())
a=[int(i) for i in input().split()]
for j in range(0,len(a)):
	if a[j]==k:
		print("yes")
		break
else:
	print("no")
