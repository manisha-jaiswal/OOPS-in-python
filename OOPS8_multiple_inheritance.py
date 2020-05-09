class Employee:
    no_of_leaves=8
    var=8
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
class Player:
    no_of_games=4
    var=9
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetail(self):
        return f"the name is {self.name} and game is {self.game}"

class Coolprogrammer(Employee,Player):
    var=10
    language="C++"
    def printl(self):
        print(self.language)
a=Employee("Manisha",50000,"Programmer")
b=Employee("Manu",51000,"tester")
s=Player("Shreya","Cricket")
m=Coolprogrammer("Salaman",50000,"CoolProgrammer")
det = m.printdetails()
m.printl()
print(m.var)
print(det)
