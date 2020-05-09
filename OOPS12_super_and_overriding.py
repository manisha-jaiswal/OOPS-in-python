#we use super for accesing super class variable
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    #pass
    classvar1 = "I am in class B"
    def __init__(self):
        #super().__init__()
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        print(super().classvar1)
a = A()
b = B()
print(b.classvar1)
print(b.special) #-error bcoz of override
print(b.special, b.var1, b.classvar1)