st = input("enter the string ")
n = ''
for i in st:
    if i.isupper():
      n+= i.lower()
    else:
       n+= i.upper()
print(n)