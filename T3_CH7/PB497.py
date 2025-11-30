# Write a python program to create a directory and subdirectory. It should print the current working directory path 
# and list of names of files present in the given directory.

import os
# Create directory
os.mkdir("MyDir")
# Create subdirectory inside it
os.mkdir("MyDir/SubDir")
# Print current working directory
print("Current Path:", os.getcwd())
# List files inside MyDir
print("Contents of MyDir:", os.listdir("MyDir"))