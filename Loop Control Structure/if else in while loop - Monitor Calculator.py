#bigger while loop to keep running programme 
exitprog = "no"
while exitprog == "no":
    #smaller while loop to keep asking inputs instead of printing area and perimeter 
    ans = "no"
    while ans == "no":
        
        length = input("Enter Length of Monitor Display in cm")
        width = input("Enter Width of Monitor Display in cm")

        print("Length is " + str(length) + " and width is " + str(width))

        ans = input("Would you like to continue? Yes or No?")

    monitorarea = (int(length) * int(width))
    #monitorarea must be converted to string type for the below style of concatenation
    print("Monitor Display Area is " + str(monitorarea) + " cm2")

    monitorperimeter = (int(length) * 2 + int(width) * 2)
    print("Monitor Display Perimeter is " + str(monitorperimeter) + " cm")    

    exitprog = input("Would you like to exit the programme? Yes or No?")
