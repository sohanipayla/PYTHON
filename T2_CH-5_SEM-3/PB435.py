l = [-1, 2, -3, 5, 7, 8, 9, -10]
l.sort(key = lambda x: (x < 0, abs(x)))
print(l)