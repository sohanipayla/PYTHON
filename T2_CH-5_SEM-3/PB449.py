str = input("Enter string: ")
list = str.split()
dict = {}
for word in list:
    key = word[0]
    if key not in dict.keys():
        dict[key] = []
    dict[key].append(word)
print(dict)