# Write a function cust_data() to ask user to enter their names and age to store data in customer.txt file

def cust_data():
    with open("customer.txt", "a") as file:
        name = input("Enter name: ")
        age = input("Enter age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    print("Data enter successfully!")
cust_data()