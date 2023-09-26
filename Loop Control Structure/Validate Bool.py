exitprog = False
while exitprog == False:
    exitprog = input("Exit program?")
    if exitprog.lower() == "yes":
        exitprog = True
    elif exitprog.lower() == "no":
        exitprog = False
    while isinstance(exitprog, bool) == False:
        exitprog = input("Exit program?")
        if exitprog.lower() == "yes":
            exitprog = True
        elif exitprog.lower() == "no":
            exitprog = False
    
        
