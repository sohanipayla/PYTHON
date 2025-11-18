l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(l) // 2:
    l[i], l[-1-i] = l[-1-i], l[i]
    i += 1
print(l)