n = input("Enter the name of the ac holder:")
acno = int(input("\nEnter the account no:"))
actype = input("\nEnter the type of account:")
bal = int(input("\nEnter the bank balance:"))
class bank:
    def __init__(self, w, x, y, z):
        self.n = w
        self.acno = x
        self.actype = y
        self.bal = z
    def dep(self,a):
        self.bal += a
    def wd(self, b):
        self.bal -= b
    def pd(self):
        print("Balance", self.bal)
obj1 = bank(n, acno, actype, bal)
damt = int(input("\nEnter the amount to deposit:"))
obj1.dep(damt)
obj1.pd()
wdamt = int(input("\nEnter the amount to withdraw:"))
obj1.wd(100)
obj1.pd()

