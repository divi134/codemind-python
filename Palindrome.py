n=int(input())
rev=0
o=n
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==o:
    print('True')
else:
    print('False')