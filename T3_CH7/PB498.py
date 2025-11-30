# Write a python program to make a module named cal.py which contain all the basic functions related to calculator like 
# addition, subtraction, multiplication, and division import that module in another file and use that functions with number 
# inputs given by user

import cal498

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print("Addition =", cal498.add(x, y))
print("Subtraction =", cal498.sub(x, y))
print("Multiplication =", cal498.mul(x, y))
print("Division =", cal498.div(x, y))