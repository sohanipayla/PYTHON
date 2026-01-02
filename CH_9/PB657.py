from abc import ABC, abstractmethod
# 1. Employee Class 
class Employee(ABC):
    def get_details(self):
        self.id = input("Employee ID: ")
        self.name = input("Employee Name: ")
        self.salary = float(input("Employee Basic Salary: "))
    def show_details(self):
        print(f"Employee ID: {self.id}")
        print(f"Employee Name: {self.name}")
        print(f"Employee Basic Salary: {self.salary}")
    def get_salary(self):
        return self.salary
    @abstractmethod
    def emp_id(self):
        pass
# 2. Perks Class 
class Perks(Employee):
    def calculate_perks(self):
        basic = self.get_salary()
        self.da = basic * 0.35  # 35% DA
        self.hra = basic * 0.17 # 17% HRA
        self.pf = basic * 0.12  # 12% PF
        self.total_perks = self.da + self.hra - self.pf
    def show_perks(self):
        print(f"DA: {self.da}")
        print(f"HRA: {self.hra}")
        print(f"PF: {self.pf}")
    def emp_id(self):
        return self.id
# 3. NetSalary Class 
class NetSalary(Perks):
    def calculate_net(self):
        self.net_salary = self.get_salary() + self.total_perks
    def display_all(self):
        self.show_details() 
        self.show_perks()   
        print(f"Total Salary: {self.net_salary}")
obj = NetSalary()
obj.get_details()
obj.calculate_perks()
obj.calculate_net()
print("\n--- Salary Slip ---")
obj.display_all()