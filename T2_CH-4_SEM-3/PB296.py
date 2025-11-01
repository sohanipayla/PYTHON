str = input("Enter the string: ")
i = int(input("Enter index: "))
str = str[:i] + str[i+1:]
print(str)