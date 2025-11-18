def common_prefix(list):
    if not list:
        return -1
    prefix = list[0]
    for s in list[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return -1
    return prefix
n = int(input("Enter number of strings: "))
list = []
print("Enter the strings:")
for i in range(n):
    list.append(input())
print("The longest Common Prefix is:", common_prefix(list))