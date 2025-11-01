n=int(input('enter number:'))
sum=0
for i in range(1,n+1):
    sum=sum+i
avg=sum/n if n>0 else 0
print('sum=',sum)
print('avg=',avg)