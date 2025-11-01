str = input("Enter the string: ")
sum = 0
c = 0
for i in str:
    if i.isdigit():
        sum += int(i)
        c += 1
avg = sum / c
print(f"sum is {sum}")
print(f"Average is {avg}")