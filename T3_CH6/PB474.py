# Write a python program to search for a string in text files.

def search():
    search_str = input("Enter the string to search: ")
    found = False
    with open('friends.txt', "r") as f:
        for line_no, line in enumerate(f, start=1):
            index = line.find(search_str)
            if index != -1:
                print(f"String found in line {line_no} at index {index}")
                found = True
    if not found:
        print("String not found in the file.")

search()