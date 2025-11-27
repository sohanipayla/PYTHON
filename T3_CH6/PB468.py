# Write a function display_oddLines() to display odd number lines from the text file. Consider the following lines for the file – friends.txt.

def display_oddLines():
    with open("friends.txt", "r") as file:
        lines = file.readlines()
        print("Odd numbered lines:")
        for i in range(0, len(lines), 2):  
            print(lines[i].strip())
display_oddLines()