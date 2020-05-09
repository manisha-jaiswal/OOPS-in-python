class Employee:
    no_of_leaves=8
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"the name is {self.name} , salary is {self.salary} and role is {self.role}"
a=Employee("Manisha",255,"Programmer")
#print(a.name , a.salary , a.role)
print(a.printdetails())