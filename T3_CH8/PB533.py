class Student:
    def __init__(self):
        self.data = []     # list to store students
    def accept(self):
        name = input("Enter Name: ")
        roll = int(input("Enter Roll Number: "))
        m1 = float(input("Enter Marks 1: "))
        m2 = float(input("Enter Marks 2: "))
        self.data.append([name, roll, m1, m2])
        print("Student Added!")
    def display(self):
        if len(self.data) == 0:
            print("No students found!")
            return
        print("\n--- Student List ---")
        for s in self.data:
            print("Name:", s[0])
            print("Roll Number:", s[1])
            print("Marks1:", s[2])
            print("Marks2:", s[3])
            print("-------------------")
    def search(self):
        r = int(input("Enter Roll Number to search: "))
        for s in self.data:
            if s[1] == r:
                print("\nStudent Found!")
                print("Name:", s[0])
                print("Roll:", s[1])
                print("Marks1:", s[2])
                print("Marks2:", s[3])
                return
        print("Student not found!")
    def delete(self):
        r = int(input("Enter Roll Number to delete: "))
        for s in self.data:
            if s[1] == r:
                self.data.remove(s)
                print("Record Deleted!")
                return
        print("Student not found!")
    def update(self):
        old = int(input("Enter OLD Roll Number: "))
        new = int(input("Enter NEW Roll Number: "))
        for s in self.data:
            if s[1] == old:
                s[1] = new
                print("Roll Number Updated!")
                return
        print("Student not found!")
obj = Student()
while True:
    print("\n1. Accept")
    print("2. Display")
    print("3. Search")
    print("4. Delete")
    print("5. Update")
    print("6. Exit")
    ch = input("Enter choice: ")
    if ch == '1':
        obj.accept()
    elif ch == '2':
        obj.display()
    elif ch == '3':
        obj.search()
    elif ch == '4':
        obj.delete()
    elif ch == '5':
        obj.update()
    elif ch == '6':
        break
    else:
        print("Wrong Choice!")