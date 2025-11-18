lst = ['abc','xyz','aba','2112','123451','12345']
count = 0
for i in lst:
    if len(i) >= 3:
        if i[0] == i[-1]:
            count += 1
print(count)