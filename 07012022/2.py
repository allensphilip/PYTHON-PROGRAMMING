#class rectangle
x = int(input("Enter the length of the first rectangle:"))
y = int(input("\nEnter the breadth of the first rectangle:"))
x1 = int(input("\nEnter the length of the second rectangle:"))
y1 = int(input("\nEnter the breadth of the second rectangle:"))
class rect:
    def __init__(self, xx, yy):
        self.a = xx
        self.b = yy
        self.per = 2 * (self.a + self.b)
        self.area = self.a * self.b
    def are(self):
        print("Area:", self.area)
    def per1(self):
        print("Peremeter:", self.per)
    def compare(self, obj):
        aes1 = self.area
        aes2 = obj.area
        if(aes1 == aes2):
            print("The two rectangles have same area")
        else:
            print("The areas are not equal")
obj1 = rect(x, y)
obj2 = rect(x1, y1)
obj1.are()
obj1.per1()
obj2.are()
obj2.per1()
obj1.compare(obj2)

