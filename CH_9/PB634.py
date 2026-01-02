class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def putdata(self):
        print(f"  - Student: {self.name}, Email: {self.email}")
class PhDguide:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.students = [] 
    def add(self, std_obj):
        self.students.append(std_obj)
    def remove(self, std_obj):
        if std_obj in self.students:
            self.students.remove(std_obj)
    def putdata(self):
        print(f"\nGuide Name: {self.name}, Email: {self.email}")
        print("List of Students:")
        if not self.students:
            print("  No students assigned.")
        for s in self.students:
            s.putdata() 
s1 = Student("Rahul", "rahul@abc.com")
s2 = Student("Sana", "sana@xyz.com")
guide = PhDguide("Dr. Sharma", "sharma@uni.com")
guide.add(s1)
guide.add(s2)
guide.putdata() 
guide.remove(s1)
print("\n--- After Removing Rahul ---")
guide.putdata() 