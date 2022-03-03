#From a list of integers, create a list removing even numbers
lim = int(input("Enter the limit of list: "))
print("Enter the elements: ")
lst = [int(input()) for i in range(lim)]
sum1 = 0
# add = [sum1 for i in lst: sum1= sum1+i]
# print(add)
for i in lst:
    sum1 = sum1 + i
print("The sum of all numbers in the is: ", sum1)