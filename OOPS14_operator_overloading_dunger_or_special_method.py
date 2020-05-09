#MAPPING OPERATORS TO FUNCTIONS
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other): #this is called dunger unit, syntax(__name__)
        return self.salary + other.salary

    def __truediv__(self, other): #truediv is used for division
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
        #return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    def __str__(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

emp1 =Employee("Harry", 345, "Programmer")
#emp2 =Employee("Rohan", 55, "Cleaner")
#print(emp1+emp2)  #operator overloading
#print(emp1 / emp2)
#print(emp1)
#print(repr(emp1))
print(str(emp1))