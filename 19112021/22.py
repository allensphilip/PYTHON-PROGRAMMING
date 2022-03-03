#Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.
list1 = []
str1 = input("Enter a string:")
print("Origial String:", str1)
f = str1[0]
str2 = str1.replace(f, "$")
str2 = f+str2[1:]
print("Character replaced string:", str2)


