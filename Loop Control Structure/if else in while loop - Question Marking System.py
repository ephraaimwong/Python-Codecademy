prompt = "Please enter marks for question "
question = 0
total = 0
exitprog = False
while exitprog == False:
    while question < 5:
        question += 1
        marks = int(input(f"{prompt}{question}:"))
        total += marks
    print("Total marks:", total)
    
    if total < 50:
        print("Student has failed the subject")
        questionloop = True
    elif total >= 50:
        print("Student has passed the subject")
        questionloop = True

    exitprog = input("Exit program?")
    if exitprog.lower() == "yes":
        exitprog = True
    elif exitprog.lower() == "no":
        exitprog = False
        question = 0 #resetting this will allow the marks input to be reprompted

    else:
        exitprog = input('''
    Invalid input
    Exit program?
        ''')