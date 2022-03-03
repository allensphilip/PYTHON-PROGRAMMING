#program to reate a string from given string where first and last characters exchanged. [eg: python - nythop]
str1 = input("Enter a string: ")
a = str1[0]
b = str1[1: -1]
c = str1[-1]
str2 = c+b+a
print("Resulted String: ", str2)
