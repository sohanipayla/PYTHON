# Write a python program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program
# creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary to identify the sender with the maximum count(the most prolific sender).

data = """From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
From louis@media.berkeley.edu Fri Jan 4 18:10:48 2008
From zqian@umich.edu Fri Jan 4 16:10:39 2008
From rjlowe@iupui.edu Fri Jan 4 15:46:24 2008
From cwen@iupui.edu Fri Jan 4 15:03:23 2008
From cwen@iupui.edu Fri Jan 4 15:01:15 2008
From cwen@iupui.edu Fri Jan 4 14:56:23 2008
From gsilver@umich.edu Fri Jan 4 14:50:18 2008
From gsilver@umich.edu Fri Jan 4 14:38:23 2008
From wagnermr@iupui.edu Fri Jan 4 14:30:44 2008
From antranig@caret.cam.ac.uk Fri Jan 4 14:28:08 2008
From gopal.ramasammycook@gmail.com Fri Jan 4 14:28:07 2008
From david.horwitz@uct.ac.za Fri Jan 4 14:28:06 2008
From david.horwitz@uct.ac.za Fri Jan 4 14:28:05 2008
From david.horwitz@uct.ac.za Fri Jan 4 14:28:04 2008
From ray@media.berkeley.edu Fri Jan 4 14:28:03 2008
"""
with open("mbox-short.txt", "w") as f:
    f.write(data)
print("File created successfully!\n")
f = open("mbox-short.txt")
count = {}
for line in f:
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        count[email] = count.get(email, 0) + 1
max_sender = max(count, key=count.get)
max_count = count[max_sender]
print(count)
print(max_sender, max_count)