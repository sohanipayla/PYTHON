# Write a python program to create and read the city.txt file in one go and print the contents on the output screen.

with open("city.txt", "w+") as file:
    file.write("Mumbai\n")
    file.write("Delhi\n")
    file.write("Pune\n")
    file.write("Bangalore")
    file.seek(0) # Move cursor to the beginning before reading
    data = file.read()
    print(data)