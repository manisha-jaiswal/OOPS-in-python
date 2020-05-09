class Dad:
    basketball=1
class Son(Dad):
    dance=1
    def isdance(self):
        return f"yes I dance {self.dance} no. of time"
class Grandson(Son):
    dance=6
    #basketball = 9
    def isdance1(self):
        return f"Jackson yeah" f"YEs i dance very awesome {self.dance} no. of times"
a=Dad()
b=Son()
c=Grandson()
print(c.isdance())
print(c.isdance1())
print(c.basketball)