
from Employee import Employee

class Manager(Employee):
    def __init__(self,name,base_salary,incentive,yearsofexperience):
        super().__init__(name,base_salary)
        self.incentive = incentive
        self.yearsofexperience = yearsofexperience
    def calculate_salary(self):
        manager_salary = self.base_salary * self.yearsofexperience + self.incentive
        return manager_salary
