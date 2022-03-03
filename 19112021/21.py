#A-Generate positive list of numbers from a given list of integer
list1 = []
list2 = []
list3 = []
list4 = []
list5 = []
list6 = []
list7 = []
n = int(input("Enter the limit:"))
list1= [int(input()) for i in range(0,n)]
#for i in range(0, n):
# ele = int(input())
#  list1.append(ele)
#    n = int(input("Enter the limit:"))
list2 = [i for i in list1 if i > 0]
#for i in range(0, n):
 #   if list1[i] > 0:
 #       list2.append(list1[i])
print(list2)
#B-Square of N numbers
n = int(input("Enter the limit:"))
list3 = [int(input()) for i in range(0, n)]
list4 = [i*i for i in list3]
print(list4)

#C-Form a list of vowels selected from a given word

w = input("Enter a word:")
list5 = [i for i in w if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U"]

print(list5)

#D-List ordinal value of each element of a word (Hint:use ord() to get ordinal values)

word = (input("Enter a word:"))
list6 = [ord(i) for i in word]
print(list6)