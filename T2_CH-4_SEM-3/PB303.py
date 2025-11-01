str = input("Enter the string: ")
words = str.split()
newStr = ""
for i in words:
    if len(i) > 2:
        newStr += i[0].upper() + i[1:-1] + i[-1].upper() + " "
    else:
        newStr += i.upper() + " "
print(newStr)