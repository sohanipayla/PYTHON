import math

def encode(str, gap):    
    encoded = ""
    for g in range(gap):
        encoded += str[g::gap]
    return encoded
def decode(str, gap):
    numCols = math.ceil(len(str) / gap)
    numRows = gap
    numShadedBoxes = (numCols * numRows) - len(str)
    plainText = [""] * numCols
    col = 0
    row = 0
    for symbol in str:
        plainText[col] += symbol
        col += 1
        if (
            (col == numCols)
            or (col == numCols - 1)
            and (row >= numRows - numShadedBoxes)
        ):
            col = 0
            row += 1
    return "".join(plainText)
def getDict(str):
    list = str.lower().split()
    dict = {}
    for word in list:
        key = word[0]
 
        if key not in dict.keys():
            dict[key] = []
        dict[key].append(word)
    sorted_list = sorted(dict.items(), key = lambda x: len(x[1]), reverse = True)
    dict = {}
    for i in sorted_list:
        key = i[0]
        value = i[1]
        dict[key] = value
    return dict
ch = input("1. Encrypt\n2. Decrypt\n3. Get Dictionary\nEnter your choice: ")
str = input("Enter the string: ")
if ch == '1':
    gap = int(input("Enter the gap: "))
    print(encode(str, gap))

elif ch == '2':
    gap = int(input("Enter the gap: "))
    print(decode(str, gap))

elif ch == '3':
    print(getDict(str))

else:
    print("Invalid choice.")