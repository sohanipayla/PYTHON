def amstrong(n):
    sum=0
    temp=0
    digits=len(str(n))
    while temp>0:
        r=temp%10
        sum=sum+r**digits
        temp//=10
        return sum==n
x=int(input('enter number:'))
print('amstrong' if amstrong(x) else 'not Amstrong')