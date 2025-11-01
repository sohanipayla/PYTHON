num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
num3=int(input('enter num3:'))
if num1>=num2 and num1>=num3:
    print('The maximum num is:',num1)
elif num2>=num1 and num2>=num3:
    print('The maximum num is:',num2)
else:
    print('The maximum num is:',num3)