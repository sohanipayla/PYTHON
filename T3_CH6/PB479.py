# Write a Python program to count words, characters and spaces from text file.

f = open("MyText.txt", "w")
f.write("Python is a Easy Subject\nOOPs is One of the most\ninteresting Topic")
f.close()
f = open("MyText.txt", "r")
data = f.read()
f.close()
space_count = data.count(" ") # Count spaces
words = data.split() # Count words
word_count = len(words)
char_count = 0 # Count characters 
for ch in data:
    if ch != "\n":
        char_count += 1
print("No of space:", space_count)
print("No of word:", word_count)
print("No of character:", char_count)