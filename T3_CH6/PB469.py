# Write a Python program to read a text file and do following: 1. Print no. of words 2. Print no. statements

def count():
    with open("friends.txt", "r") as file:
        text = file.read()
    # 1. Count words
    words = text.split()
    print("Number of words:", len(words))
    # 2. Count Statements
    statements = text.split('!')
    print('Number of statments:',len(statements)-1)
count()