a=int(input())
b=int(input())
for i in range(a,b+1):
    rev=0
    temp=i
    while temp>0:
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if i==rev:
        print(i,end=' ')