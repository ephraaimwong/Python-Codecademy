sindex = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
allmarks = [40, 60, 70, 55, 62, 70, 50, 80, 88, 56]

def showMenu():
    print("="*40, '''
Please choose option:
A - Display students' marks
B - Display highest score
Q - Exit program
''', "="*40)

def dispMarks():
    for index, marks in zip(sindex, allmarks):
        print(f"Student Index No:{index:2} Marks: {marks:2}")

def dispMax():
    maxmark, maxindex = 0, 0
    maxmark = max(allmarks) #gets the largest value from allmarks list
    maxindex = allmarks.index(maxmark) #gets the index of the maxmark
    print(f"Highest Score student index No:{maxindex+1} Marks:{maxmark}")#{maxindex+1} since indexes start from 0.

exitprog = False
while exitprog == False:
    progchoice = input(showMenu())
    if progchoice.lower() == "a":
        print(dispMarks())
    elif progchoice.lower() == "b":
        print(dispMax())
    elif progchoice.lower() == "q":
        print("Goodbye.")
        exitprog = True
    else:
        progchoice = input("Invalid input. Please try again.")