#Print out all colors from Set1 not contained in Set2.
n1 = int(input("Enter the limit of first set: "))
print("Enter the elements:")
s1 = {(input()) for i in range(n1)}
n2 = int(input("Enter the limit of Second set: "))
print("Enter the elements:")
s2 = {(input()) for j in range(n2)}
print("Set 1: ", s1)
print("Set 2: ",s2)
s3 = s1.difference(s2)
print("Colors only in set1 not in set2 are:", s3)