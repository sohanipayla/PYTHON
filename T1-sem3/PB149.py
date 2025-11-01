num1=int(input('enter num1:'))
num2=int(input('enter num2:'))
num3=int(input('enter num3:'))
count=0
for i in range(num1,num2+1):
    if i%num3==0:
        count=count+1
print(num1,num2,num3,count)