from abc import ABC, abstractmethod
class Employee(ABC):
    def display(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
    @abstractmethod
    def display(self):
        pass
class Perks(Employee):
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary 
        self.DA = 0.35 * self.salary
        self.HRA = 0.17 * self.salary
        self.PF = 0.12 * self.salary
    def display(self):
        print(f"DA: {self.DA}")
        print(f"HRA: {self.HRA}")
        print(f"PF: {self.PF}")
    def get_total_perks(self):
        return self.DA + self.HRA - self.PF
class NetSalary:
    def __init__(self, perks):
        self.perks = perks 
    def display(self):
        print(f"Employee ID: {self.perks.emp_id}")
        print(f"Name: {self.perks.name}")
        print(f"Basic Salary: {self.perks.salary}")
        self.perks.display()
        print(f"Total Salary: {self.perks.salary + self.perks.get_total_perks()}")
perks = Perks(1, "John", 25000)
net_salary = NetSalary(perks)
net_salary.display()
