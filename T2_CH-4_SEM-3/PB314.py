text = input("Enter the text to encrypt: ")
shift = int(input("Enter shift value: "))
result = ""
for ch in text:
    if ch.isupper(): 
        result += chr((ord(ch) - 65 + shift) % 26 + 65)
    elif ch.islower(): 
        result += chr((ord(ch) - 97 + shift) % 26 + 97)
    else:  
        result += ch
print("Encrypted text:", result)
