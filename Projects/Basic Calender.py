from time import *
prompt = '''
1 - View the calendar
2 - Add an event to the calendar
3 - Update an existing event
4 - Delete an existing event
Q - Exit program
'''
calender = {}
def validate_date(date):
    if len(date) > 10:
        date = input("Invalid input, try again")
    elif len(date) < 10:
        date = input("Invalid input, remember to include the /'s ")
    else:
        return date

username = input("Enter username: ")
currentdate = strftime("%m/%d/%Y, %H:%M:%S")
exitprog = False
while exitprog == False:
    optionsel = input(prompt)
    if optionsel == "1":
        if len(calender.keys()) < 1:
            optionsel = input("Calender is currently empty" + prompt)
        else:
            print(calender)
    elif optionsel == "2":
        event = input("Enter event: ")
        date = input("Enter date(MM/DD/YYYY): ")
        validate_date(date)
        if int(date[6:]) < int(strftime("%Y")):
            try_again = input('''Invalid input
            Scheduling past dates is not available
Try again? (Y/N)''')
            if try_again.lower() == "y":
                continue
            if try_again.lower() == "n":
                optionsel = input(prompt)
            else:
                calender[date] = event
                print(f"{calender[date]} has been added: {date}.")
                optionsel = input(prompt)
    elif optionsel == "3":
        date = input("Enter date(MM/DD/YYYY): ")
        update = input("Enter update: ")
        validate_date(date)
        calender[date] = update
        print(f"{calender[date]} has been updated: {date}.")
    elif optionsel == "4":
        date = input("Enter date(MM/DD/YYYY): ")
        if len(calender.keys()) < 1:
            optionsel = input("Calender is empty", prompt)
        else:
            event = input("Enter event: ")
            for i in calender.keys():
                if event == calender.keys():
                    del calender[date]
                    optionsel = input(f"{event} has been deleted.")
                else:
                    try_again = input('''Invalid input
That event does not exist
Try again? (Y/N)''')
                    if try_again.lower() == "y":
                        continue
                    if try_again.lower() == "n":
                        optionsel = input(prompt)

    elif str(optionsel.lower()) == "q":
        print("Goodbye!")
        exitprog == True
