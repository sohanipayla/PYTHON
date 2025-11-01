def find_length(string):
    count = 0
    for i in string:
        count = count + 1
    return count
s = input("Enter a string: ")
length = find_length(s)
print("Length of the string is:", length)