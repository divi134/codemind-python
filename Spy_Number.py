n=int(input())
s=0
p=1
while n>0:
    digit=n%10
    s=s+digit
    p=p*digit
    n=n//10
if p==s:
    print('Spy Number')
else:
    print('Not Spy Number')
