# Write a python program to read a text file “Story.txt” and print only word starting with ‘I’ in reverse order.

f = open("Story.txt", "w")
f.write("INDIA IS MY COUNTRY")
f.close()
f = open("Story.txt", "r")
data = f.read()
f.close()
words = data.split()
new_list = []

for w in words:
    if w.startswith("I"):       
        new_list.append(w[::-1])  
    else:
        new_list.append(w)         
result = " ".join(new_list)
print(result)