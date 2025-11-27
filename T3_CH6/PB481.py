# Write a python program to accept string/sentence from user till the user enters “END”. Each string/sentence entered by 
# user should be a newline in file. Save all the lines in file and display only those lines which begin with capital letter.

f = open("UserLines.txt", "w")
while True:
    text = input("Enter Something: ")
    if text == "END":
        break
    f.write(text + "\n")
f.close()
print("The Line started with Capital Letters:")
f = open("UserLines.txt", "r")
lines = f.readlines()
f.close()
for line in lines:
    if len(line) > 0 and line[0].isupper():
        print(line.strip())