# Write a program to compare two text files. If they are different, give the line and column numbers in the files where the 
# first difference occurs.

f1 = open("python1.txt", "w")
f1.write("Friends are crazy, Friends are naughty !\n"
         "Friends are honest, Friends are best !\n"
         "Friends are like keygen, friends are like license key !\n"
         "new We are nothing without friends, Life is not possible without friends !")
f1.close()
f2 = open("python2.txt", "w")
f2.write("Friends are crazy, Friends are naughty !\n"
         "Friends 6re honest, Friends are best !\n"
         "Friends are like keygen, friends are like license key !\n"
         "new We are nothing without friends, Life is not possible without friends !")
f2.close()

f1 = open("python1.txt", "r")
f2 = open("python2.txt", "r")
line_no = 0
found = False
while True:
    line1 = f1.readline()
    line2 = f2.readline()
    line_no += 1
    if not line1 or not line2:
        break
    if line1 != line2:          
        for i in range(len(line1)):
            if i >= len(line2) or line1[i] != line2[i]:
                print("line number", line_no, "colNo.", i+1)
                found = True
                break
        break
if not found:
    print("Files are identical")
f1.close()
f2.close()