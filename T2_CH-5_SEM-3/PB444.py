def validity1(pas):
    return len(pas) >= 8
def validity2(pas):
    return not(pas.islower()) and not(pas.isupper())
def validity3(pas):
    for i in pas:
        if i.isdigit():
            return True
    return False
password = input("Enter the password: ")
if validity1(password):
    if validity2(password):
        if validity3(password):
            print("Password is valid")
        else:
            print("Number missing")
    else:
        print("Both upper and lower case required")
else:
    print("Min 8 chars required")