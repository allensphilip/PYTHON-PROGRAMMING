#program to print leap year from current year to a limit
final = int(input("Enter the final year:"))
i = 2020
while i <= final:
    i = i+4
    if i <= final:
        if i % 100 != 0:
            print(i,)
        elif i % 400 == 0:
            print(i,)
    i = i

