def product(n):
    pro=1
    for i in range(1,n+1):
        pro=pro*i
    return pro
x=int(input('enter number:'))
print('multiplication:',product(x))    