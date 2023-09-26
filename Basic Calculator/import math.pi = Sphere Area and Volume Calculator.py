exit_prog = "no"
while exit_prog.lower() == "no":
    sphere_inputs = "no"
    while sphere_inputs.lower() == "no":
        #radius must be converted to float when calculated with other floats or **
        sphere_radius = float(input("Please enter the radius of sphere."))
        print("Radius entered is", sphere_radius, "cm2.")
        sphere_inputs = input("Would you like to continue? Yes or No?")

    import math
    pi = math.pi
    sphere_surface = 4 * pi * sphere_radius **2
    #round(variable,decimalplace) for specs of project
    print("Surface area of the sphere is", round(sphere_surface,2), "cm2.")
    sphere_volume = (4/3) * (pi * sphere_radius **3)
    print("Volume of the sphere is", round(sphere_volume,2), "cm3.")

    exit_prog = input("Would you like to exit the programme? Yes or No?")