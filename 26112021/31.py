#From a list of integers, create a list removing evennumbers
lim = int(input("Enter the limit:"))
print("Enter the elements:")
l1 = [int(input()) for i in range(lim)]
print("Entered list: ",l1)
l2 = [j for j in l1 if j % 2 != 0]
print("List after removing even numbers: ",l2)