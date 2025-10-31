# Employee Management:
# Create a base class Employee with attributes like name , salary and a method calculate_salary().
# Inherit from this class to create subclasses RegularEmployee, ContractEmployee, and Manager.
# Each subclass should have specific attributes and calculations for salary.
# Implement inheritance and polymorphism to calculate the salary of different employee
# types based on their specific
# attributes and rules

class Employee:
    def __init__(self,name,base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.salary

    def __str__(self):
        return f"{self.__class__.__name__} - Name: {self.name}, Salary: ₹{self.calculate_salary():,.2f}"

