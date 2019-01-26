#273.15
c=int(input())
k=c+273.15
for i in range(0,len(k)):
	if k[i]==".":
		break
print(k)
