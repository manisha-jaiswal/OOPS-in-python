class Employee:
    no_of_leaves=8
    def printdetails(self):
        return f"My Name is {self.name} and salary is {self.salary}"
a=Employee()
b=Employee()
a.name="Manu"
a.salary=500

b.name="Saam"
b.salary=600
print(a.printdetails())
print(b.printdetails())
print(a.no_of_leaves)