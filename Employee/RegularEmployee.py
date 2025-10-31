from Employee import Employee
class RegularEmployee(Employee):
    def __init__(self,name,base_salary,incentive):
        self.name = name
        self.base_salary = base_salary
        self.incentive = incentive
    def calculate_salary(self):
        RegularEmployee_salary = self.base_salary + self.incentive
        return RegularEmployee_salary
