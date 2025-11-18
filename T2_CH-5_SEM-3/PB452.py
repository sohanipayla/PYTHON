lst = [1, 2, 3, 4, 5]
shift = int(input("Enter shift: "))
lst = lst[shift:] + lst[:shift]
print(lst)
 