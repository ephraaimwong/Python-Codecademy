exit_prog = "no"
while exit_prog == "no":
    height = float(input("Enter height(m):"))
    weight = float(input("Enter weight(kg):"))
    bmi = weight / height ** 2
    print("Your BMI is", round(bmi,2))
#if statements build off each other
    if bmi < 18.5:
        print("You are under weight.")
    elif bmi <= 24.9:
        print("You have a healthy weight.")
    elif bmi <= 29.9:
        print("You are overweight.")
    elif bmi > 30.0:
        print("You are obese.")

    exit_prog = input("Exit programme? Yes or No?")