from numpy import mean
openingstate = '''
Finding the sum and mean of consecutive numbers starting from 1
Please enter the final number as an integer: 
'''
startingnum = 1
exitprog = "no"
while exitprog.lower() == "no":
    finalnum = input(openingstate)
    finalnum = int(finalnum)
    for i in range(1, (finalnum + 1)):
        total = range(1, (finalnum + 1))
    #printing must be outside of the loop if not, FOR LOOP will repeat to print sum and mean
    print("Sum: ", round(sum(total),2))
    print("Mean: ", round(mean(total),2))
    exitprog = input("Exit program?")