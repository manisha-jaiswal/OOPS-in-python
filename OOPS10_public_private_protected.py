# Public (use nothing before name) - share with anyone, anyone access it
# Protected(start with _ ) - share only within the class and child of that class, outsider cannot access
# Private (start with __ )- share only within the class, outside of class not accssed

class Employee:
    no_of_leaves = 8
    var = 8 #public
    _protec = 9 #protected
    __pr = 98 #private
emp = Employee()
print(emp._protec)
#print(emp.__pr) #we cant access this bcoz it is private,it is called name mangeling ,
# if we want to acces it we use _classname__privatevariable
print(emp._Employee__pr)