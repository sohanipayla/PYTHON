# Write a python program to read line by line from a given files file1 & file2 and write into file3.

with open("file1.txt", "w") as f1:
    f1.write("A\n")
    f1.write("B\n")
    f1.write("C\n")

with open("file2.txt", "w") as f2:
    f2.write("1\n")
    f2.write("2\n")
    f2.write("3")

with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

with open("file3.txt", "w") as f3:
    for l1, l2 in zip(lines1, lines2):
        f3.write(l1)
        f3.write(l2)

print("file1 & file2 and write into file3")