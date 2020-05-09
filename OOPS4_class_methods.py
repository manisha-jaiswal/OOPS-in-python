class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.nm=name
        self.slry=salary
        self.rl=role
    def printdetails(self):
        return f"Name is {self.nm}, Salary is {self.slry} and Role is {self.rl}"
    @classmethod
    def change_leaves(cls,newleaves):#cls ek class h jiska instance h object let a,
        # it is a class method which is accesed only the class instance
        cls.no_of_leaves=newleaves
a=Employee("Manisha",50000,"Programmer")
b=Employee("Avi",70000,"Engineer")
a.change_leaves(34)
print(a.no_of_leaves)
Employee.change_leaves(55)
print(Employee.no_of_leaves)
print(a.no_of_leaves)
print(a.printdetails())