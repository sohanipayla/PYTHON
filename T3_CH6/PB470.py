# Write a python program that reads a text file and changes the file by capitalizing each character of file.

file = open('cap.txt', 'r+')
data = file.read()
data = data.upper()
file.seek(0)
file.write(data)
file.close()
print("Done!")