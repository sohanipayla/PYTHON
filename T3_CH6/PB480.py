# File Filtering. write all lines of a file1, except those that start with a pound sign ( # ), the comment character for Python to 
# file2. And display data of file2

f1 = open("file1_new.txt", "w")
f1.write("Friends are crazy, Friends are naughty !\n"
         "#Friends are honest, Friends are best !\n"
         "Friends are like keygen, #friends are like license key !\n"
         "We are nothing without friends, Life is not possible without friends !")
f1.close()
f1 = open("file1_new.txt", "r")
lines = f1.readlines()
f1.close()
f2 = open("file2_new.txt", "w")
for line in lines:
    if not line.lstrip().startswith("#"):    # ignore comment lines
        if "#" in line:    
            index = line.index("#")
            line = line[:index] + "\n"
        f2.write(line)
f2.close()
f2 = open("file2_new.txt", "r")
print(f2.read())
f2.close()
