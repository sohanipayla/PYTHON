lst = [1, 13, 2, 3, 4]
was_13 = False
sum = 0
for i in lst:
    if i == 13:
        was_13 = True
        continue
    if was_13:
        was_13 = False
        continue
    sum += i
print("Sum is ", sum)