#program to input an age and check whether the age is eligible to vote or not.

age = int(input("Enter the age of the person: "))
if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")