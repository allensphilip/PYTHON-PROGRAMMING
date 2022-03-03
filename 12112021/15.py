#Display the appropriate message as per the colour of signal at the road crossing.

color = input("Enter the colour of light signal:")
if (color == "green" or color == "GREEN"):
    print("Go")
elif (color == "yellow" or color == "YELLOW")
    print("Wait")
elif (color == "orange" or color == "ORANGE")
    print("Move Slowly")
elif (color == "red" or color == "RED")
    print("Stop")
else:
    print("Invalid signal")