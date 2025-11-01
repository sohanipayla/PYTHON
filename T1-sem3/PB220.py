def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def divi(a,b):
    return a/b
a=int(input('enter number1:'))
b=int(input('enter number2:'))
op=input('enter opretor(+,-,*,/)')
if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(multi(a,b))
elif op=='/':
    print(divi(a,b))
else:
    print('Invalid Choice')