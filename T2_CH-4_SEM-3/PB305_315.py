s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s1 = s1.lower()
s2 = s2.lower()
balanced = True 
for ch in s1:
    if ch not in s2:
        balanced = False
        break  
if balanced:
    print("Strings are balanced.")
else:
    print("Strings are not balanced.")