from Employee import Employee
from ContractEmployee import ContractEmployee
from Manager import Manager
from RegularEmployee import RegularEmployee


class Main(Employee):
    if __name__ == '__main__':
        regemp = RegularEmployee("Ajay",20000,5000)
        manag = Manager("Vijay",30000,5000,2)
        cont = ContractEmployee("Salma",2000,15,2000)
    classemp = [regemp,manag,cont]
    for emp in classemp:
        print(emp)
