#Create a single string separated with space from two strings by swapping the character at position 1
str1 = input("Enter first string: ")
str2 = input("Enter Second string: ")
s1f = str1[0]
s2f = str2[0]
s1l = str1[1:]
s2l = str2[1:]
str3 = " "
str4 = s2f + s1l + str3 + s1f + s2l
print("Merged String: ", str4)
