#WAP to enter Name, marks of 5 subject and calculate total & percentage of student

name = input("Enter the name of the student: ")
sub1 = int(input("Eneter the mark of subject 1 : "))
sub2 = int(input("Eneter the mark of subject 2 : "))
sub3 = int(input("Eneter the mark of subject 3 : "))
sub4 = int(input("Eneter the mark of subject 4 : "))
sub5 = int(input("Eneter the mark of subject 5 : "))
total = int(input("Enter the total of maximum marks of five subjects: "))
tob = sub1 + sub2 + sub3 + sub4 + sub5
per = (tob / total) * 100
print("Total Marks: ", +tob, "/", +total,  ",  ", +per, "% of mark in total")