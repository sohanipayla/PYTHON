def valid(p):
    # Conditions:
    # 1. At least 1 digit
    # 2. At least 1 uppercase
    # 3. At least 1 lowercase
    # 4. At least 1 special character from @$_
    # 5. Length between 8 and 15
    # 6. No spaces and no other special characters except @$_
    if len(p) < 8 or len(p) > 15:
        return False
    if not any(ch.isdigit() for ch in p):
        return False
    if not any(ch.isupper() for ch in p):
        return False
    if not any(ch.islower() for ch in p):
        return False
    if not any(ch in "@$_" for ch in p):
        return False
    for ch in p:
        if not (ch.isalnum() or ch in "@$_"):
            return False
    return True
d = {
    "student0": 'Student@0',
    "student1": 'Student@11',
    "student2": 'Student@121',
    "student3": 'Student@052',
    "student4": 'Student@01278',
    "student5": 'Student@0125',
    "student6": 'Student@042',
    "student7": 'Student@07800',
    "student8": 'Student@012'
}
ok = False
for i in range(3):
    u = input("Username: ")
    p = input("Password: ")
    if u in d and d[u] == p:
        ok = True
        break
    print("enter correct password and username")
if not ok:
    print("try after 24h")
    print(d)
    exit()
updated = False
for i in range(3):
    newp = input("Enter new password: ")
    if valid(newp):
        d[u] = newp
        updated = True
        break
    print("follow the password format")
if not updated:
    print("follow the password format")
    print("try after 24h")
    print(d)
    exit()
print("\nUpdated Dictionary:")
print(d)
print("\nSorted by password length:")
for k, v in sorted(d.items(), key=lambda x: len(x[1])):
    print(k, ":", v)