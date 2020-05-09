class Employee:
    no_of_leaves=8 #class variable
    pass
a=Employee() #class object
b=Employee()

a.name="Manisha" #object variable
a.salary=50,000
a.role="Tester"

b.name="Avi"
b.salary=1,99,000
b.role="Programmer"
print(a.name,a.salary,a.role,"\n",b.name,b.salary,b.role)
print(a.no_of_leaves)
print(b.no_of_leaves)
print(Employee.no_of_leaves)
a.no_of_leaves=9
print(Employee.no_of_leaves)
Employee.no_of_leaves=10
print(Employee.no_of_leaves)
print(a.__dict__)
print((Employee.__dict__))