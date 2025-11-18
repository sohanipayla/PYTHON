from functools import reduce
lst = [1, 2, 3, 4]
# Part A
tpl = tuple(map(lambda x: str(x), lst))
print(tpl)
# Part B
tpl = tuple(map(lambda x: x * 10, lst))
print(tpl)
# Part C
prod = reduce(lambda x, y: x * y, lst)
print(prod)
# Part D
def countchar(str, char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count
print(countchar("hello", "l"))
def findchar(str, char):
    ind = 0
    for i in str:
        if char == i:
            return ind
        ind += 1
    return -1
print(findchar('helloe', 'e'))