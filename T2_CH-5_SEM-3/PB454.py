str = input("Enter a string: ")
last = []
for i in str:
    if i == '(':
        last.append('(')
    elif i == '{':
        last.append('{')
    elif i == '[':
        last.append('[')
    elif i == ')':
        if last.pop() != '(':
            print("Invalid.")
            break
    elif i == '}':
        if last.pop() != '{':
            print("Invalid.")
            break
    elif i == ']':
        if last.pop() != '[':
            print("Invalid.")
            break
else:
    if len(last) == 0:
        print("Valid.")
    else:
        print("Invalid.")