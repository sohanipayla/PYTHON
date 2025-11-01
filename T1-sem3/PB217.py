def even(n):
    return n%2==0
a=int(input('enter num1:'))
b=int(input('enter num2:'))
print('first is even' if even(a) else 'first is odd')
print('second is even' if even(b) else 'second is odd')