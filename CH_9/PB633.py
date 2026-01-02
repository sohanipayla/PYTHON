class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def putdata(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
class Teaching(Staff):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject
    def putdata(self):
        super().putdata()
        print(f"Subject: {self.subject}")
class NonTeaching(Staff):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
    def putdata(self):
        super().putdata()
        print(f"Department: {self.department}")
print("--- Teaching Staff ---")
t = Teaching("Amit", 50000, "Mathematics")
t.putdata()
print("\n--- Non-Teaching Staff ---")
nt = NonTeaching("Suresh", 30000, "Administration")
nt.putdata()