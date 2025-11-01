st = input("Enter the password :: ")
l, u, d, s = 0, 0, 0, 0
if len(st) >= 8:          
    for i in st:
        if i.islower():
            l += 1
        elif i.isdigit():
            d += 1
        elif i.isupper():
            u += 1
        elif i in "@_$":
            s += 1

    if l and d and u and s:
        print("Valid password")
    else:
        print("Invalid password")
else:
    print("Invalid password — must be at least 8 characters long")