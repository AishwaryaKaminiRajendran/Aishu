n=int(input())
a=[]
s=0
for i in range(3,n):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        if i%10==3:
            s=s+i
print(s)
