str = input("Enter the string: ")
mid = len(str) // 2
str = str[:mid].upper() + str[mid:]
print(str)