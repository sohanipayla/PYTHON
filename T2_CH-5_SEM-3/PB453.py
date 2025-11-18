l = [2, 4, 6, 8, 10]
print(l)
for i in range(1, len(l)+1, 2):
  l.insert(i,l.pop())
print(l)