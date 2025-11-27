# Write a Python program to reverse the content of a one file and store it in second file and also convert content of second file into 
# uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from the content of third file.

def create_file():
    text = """Friends are crazy, Friends are naughty ! \n
Friends are honest, Friends are best !"""
    
    with open("data1.txt", "w") as f:
        f.write(text)

# Step 1: Reverse content of data1 → data2
def reverse_file():
    with open("data1.txt", "r") as f1:
        lines = f1.readlines()
    reversed_lines = [line[::-1] for line in lines]
    with open("data2.txt", "w") as f2:
        f2.writelines(reversed_lines)

# Step 2: Convert data2 → uppercase → data3
def uppercase_file():
    with open("data2.txt", "r") as f2:
        data = f2.read()
    with open("data3.txt", "w") as f3:
        f3.write(data.upper())

# Step 3: Count vowels in data3
def count_vowels():
    with open("data3.txt", "r") as f3:
        data = f3.read()
    vowels = "AEIOUaeiou"
    count = 0
    for ch in data:
        if ch in vowels:
            count += 1
    print("Vowels =", count)

# Step 4: Print only second line from data3
def second_line():
    with open("data3.txt", "r") as f3:
        lines = f3.readlines()
    print(lines[1].rstrip())   # 2nd line only

create_file()
reverse_file()
uppercase_file()
count_vowels()
second_line()