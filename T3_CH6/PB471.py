# Write a Python program to copy the contents of a file to another file

with open("source.txt", "w+") as f1:
    f1.write("This is new content.\n")
    f1.write("We are creating a file and copying it.")
    f1.seek(0)
    data = f1.read()

with open("destination.txt", "w") as f2:
    f2.write(data)

print("File copied successfully!")