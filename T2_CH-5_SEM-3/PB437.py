list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]
dict = {}

for i in list:
    if i not in dict:
        dict[i] = [i]
    else:
        dict[i].append(i)
sorted_items = sorted(dict.i(), key=lambda x: len(x[1]), reverse=True)
sorted_dict = dict(sorted_items)
print(sorted_dict)