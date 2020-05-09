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
    @classmethod
    def from_dash(cls,string):
        #params=string.split("-")
        #print(params)
        #return cls(params[0],params[1],params[2])
        return cls(*string.split("-")) #here we write above 3 lines in a single line


a=Employee("Manisha",50000,"Programmer")
k=Employee.from_dash("karan-400-Student")
print(k.slry)
print(k.nm)
print((k.rl))
#a.change_leaves(34)
#print(a.no_of_leaves)
