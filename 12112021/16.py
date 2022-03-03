#program to create a simple calculator performing only four basic operations.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
opt = int(input("Choose an option:\n 1. Addition\n 2. Subtraction\n 3. Multiply\n 4. Division\nChoose your option"))
if opt == 1:
    c = a+b
    print("Sum : ", +c)
elif opt == 2:
    c = a-b
    print("Difference : ", +c)
elif opt == 3:
    c = a*b
    print("Product : ", +c)
elif opt == 4:
    c = a/b
    print("Division : ", +c)
else:
    print("Invalid option")
