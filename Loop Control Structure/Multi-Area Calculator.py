menu = '''
=================================
Calcute Area
Please choose one from the following
A - Area of Rectangle
B - Area of Right-angled Triangle
C - Area of Circle
Q - Exit Program
'''
import math
exitprog = "no"
while exitprog.lower() == "no":
    selectcal = input(menu)
    
    if selectcal.lower() == "a":
        rectlength = input("Input length of the rectangle: ")
        rectwidth = input("Input width of the rectangle: ")
        rectarea = float(rectlength) * float(rectwidth)
        print("Area of the rectangle is:", round(rectarea,1))

    elif selectcal.lower() == "b":
        tribase = input("Input base of the triangle: ")
        triheight = input("Input height of triangle: ")
        triarea = float(tribase) * float(triheight)
        print("Area of the right-angled triangle is:", round(triarea,1))

    elif selectcal.lower() == "c":
        circlerad = input("Input radius of circle: ")
        circlearea = math.pi * float(circlerad) ** 2
        print("Area of the circle is:", round(circlearea,1))

    elif selectcal.lower() == "q":
        break

    else:
        print("Invalid choice. Please")

    exitprog = input("Would you like to quit?")