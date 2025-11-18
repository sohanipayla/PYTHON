str = input("Enter paragraph: ").lower()
dict = {}
lst = str.split()
for word in lst:
    if word not in dict.keys():
        dict[word] = 0
    dict[word] += 1
print(dict)