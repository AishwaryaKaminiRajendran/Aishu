a=int(input())
if a%2==0:
    while a%2==0:
        b=a//2
        print(b,end=" ")
        a=b
else:
    print(a)
