N = int(input("Enter num: "))
sum = 0
for i in range(1, N+1):
    sum += i
    avg=sum/N
print("The avg of first", N, "natural numbers is:", avg)