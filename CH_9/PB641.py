class Student:
    def __init__(self, roll_no, name, age, marks):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.marks = marks
    def display(self):
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Age: {self.age}, Marks: {self.marks}")
    # Overloading '==' operator
    def __eq__(self, other):
        return self.marks == other.marks
s1 = Student(101, "Alice", 20, 85)
s2 = Student(102, "Bob", 21, 90)
s3 = Student(103, "Charlie", 20, 85)
students = [s1, s2, s3]
print("Comparing students with same marks:\n")
if s1 == s3:
    print("S1 and S3 have the same marks. Details:")
    s1.display()
    s3.display()
if s1 == s2:
    print("S1 and S2 have same marks.")
else:
    print("\nS1 and S2 do not have the same marks.")