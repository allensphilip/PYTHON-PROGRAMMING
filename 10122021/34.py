#Program to find the factorial of a given number using user-defined function

n = int(input("Enter a number:"))
i = 1
fact1 = 1
def factfn(n):
    global fact1
    global i
    while(i <= n):
        fact1 = fact1 * i
        i = i+1
factfn(n)
print("Factorial of", n, "is : ", +fact1)

