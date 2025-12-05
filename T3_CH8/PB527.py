class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks
s1 = Student("Rahul", 85)
print("Original Name:", s1.student_name)
print("Original Marks:", s1.marks)
s1.student_name = "Aman"
s1.marks = 92
print("\nModified Name:", s1.student_name)
print("Modified Marks:", s1.marks)