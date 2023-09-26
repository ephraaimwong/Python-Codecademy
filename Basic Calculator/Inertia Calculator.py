exit_prog = "no"
while exit_prog == "no":
    input_ans = "no"
    while input_ans == "no":
        mass = float(input("Enter mass of object(kg):"))
        rad = float(input("Enter radius of object(m):"))
        print("Mass =", mass, "Radius =", rad)
        input_ans = input ("Are the values correct? Yes or No?")
#variables must all be float when calculating with other float or **
    inertia = 0.5 * float(mass) * float(rad) **2
    print("The inertia is", inertia)
    exit_prog = input("Exit programme? Yes or No?")