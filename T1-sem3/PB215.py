def fibonaci(n):
    if n==0:
        print('NO display')
    elif n==1:
        print('0')
    elif n==2:
        print('0 1')
    else:
        a,b=0,1
        print(0,1, end=' ')
        for i in range(2,n):
            c=a+b
            print(c,end=' ')
            a,b=b,c
n=int(input('enter number:'))
fibonaci(n)