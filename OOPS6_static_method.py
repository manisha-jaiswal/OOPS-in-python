class Static_method:
    @staticmethod
    def printgood(string):
        print("This Is Good ",string)

a=Static_method()
#print(a.printgood("abc")) #here it gives none bcoz printgood is not return anything
a.printgood("abc")
Static_method.printgood("Manisha")