
def reverse(n):
    rev=0
    temp=n
    while temp>0:
        r=temp%10 
        rev=rev*10+r
        temp//=10
    return rev
x=int(input('enternumber:'))
print('Reverse:',reverse(x))