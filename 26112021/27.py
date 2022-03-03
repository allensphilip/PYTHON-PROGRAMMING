#Create a list of colors from comma-separated color names entered by user. Display first and last colors.
color = input("Enter the color(Seperate them with commas) : ")
clist = color.split(",")
print("Entered colors are: ", clist)
print("First color : ", clist[0], "\nLast color : ", clist[-1])