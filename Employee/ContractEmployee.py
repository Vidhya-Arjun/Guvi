from Employee import Employee


class ContractEmployee(Employee):
    def __init__(self, name, base_salary,workinghours,mediclaim):
            super().__init__(name,base_salary)
            self.workinghours = workinghours
            self.mediclaim = mediclaim
    def calculate_salary(self):
        self.salary = (self.base_salary  * self.workinghours) - self.mediclaim
        return self.salary
