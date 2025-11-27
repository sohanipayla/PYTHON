# Write a python program to extract a list of all four-letter words that start and end with the same letter from a given text file

f = open("sample.txt", "w")
f.write("noon deed peep cool kick room test door level noon meet peep")
f.close()
f = open("sample.txt", "r")
data = f.read()
f.close()
words = data.split()
result = []
for w in words:
    w2 = w.lower()
    if len(w2) == 4 and w2[0] == w2[-1]:
        result.append(w2)
print(result)