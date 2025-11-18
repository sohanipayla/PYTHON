l= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
largest_odd = l[0]
for i in l:
    if i % 2 == 1 and i > largest_odd:
        largest_odd = i
print(largest_odd)