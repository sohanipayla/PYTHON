# Write a python program to make a module which contain all the basic functions related to string and import that module 
# in another file and use that fuctions with string given by user

import string496
text = input("Enter a string: ")
print("Length of string =", string496.string_length(text))
print("Reversed string =", string496.string_reverse(text))
print("Total vowels =", string496.vowel_count(text))
print("Uppercase =", string496.to_uppercase(text))
print("Lowercase =", string496.to_lowercase(text))