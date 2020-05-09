class Employee:
    no_of_leaves=8
    def __init__(self,name,salary,role):
        self.nm=name
        self.slry=salary
        self.rl=role
    def printdetails(self):
        return f"Name is {self.nm}, Salary is {self.slry} and Role is {self.rl}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves
    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def printgood(string):
        print("This Is Good ", string)

class Programmer(Employee):#single inheritnce
    no=5
    def __init__(self,name,salary,role,language):
        self.nm = name
        self.slry = salary
        self.rl = role
        self.languages=language
    def printprog(self):
        return f"The Programmer is {self.nm}, salary is {self.slry} , role is {self.rl} and language known is {self.languages}"

a=Employee("Manisha",50000,"Programmer")
b=Employee("Manu",51000,"tester")
c=Programmer("saam",5000,"Programmer",["python","c"])
d=Programmer("avinash",10000,"engineer","java")
print(c.printprog())
print(c.no)
print(c.printdetails())