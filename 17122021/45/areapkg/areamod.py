def area():
    from sqmod import sqarea as x
    from rectmod import rectarea as y
    print("Area of a square")
    a = int(input("Enter the side of the square: "))
    x(a)
    print("\nArea of a rectangle")
    l = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the breath of the rectangle: "))
    y(l, b)
