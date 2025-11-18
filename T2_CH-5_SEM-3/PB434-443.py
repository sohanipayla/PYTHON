n = [5, -3, 7, -2, 0, 9, -6]
positive = sum(filter(lambda x: x > 0, n))
negative = sum(filter(lambda x: x < 0, n))
print("Sum of positive numbers:", positive)
print("Sum of negative numbers:", negative)