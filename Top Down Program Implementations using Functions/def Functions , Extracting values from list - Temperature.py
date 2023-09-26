time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
temp = [41, 44, 42, 40, 38, 43, 41, 40, 42, 45, 47, 48]
avgtemplist = []

def nhouravgTemp(start,end):
    sum, avgtemp = 0, 0
    nduration = end - start + 1 # +1hr to include the ending hour, i.e. 3-1=2 but duration is 3 hrs. 
    for i in range(start - 1, end): #start-1 to reflect accurate index in temp since index start from 0, 
        sum += temp[i] #temp[i] takes the temp values between the start and end index is NOT INCLUCED
        avgtemplist.append(temp[i]) #append temp values to index
    avgtemp = sum / nduration
    print(f"Average temp from hour {start} - {end} is {avgtemp}C.")

def maxnTemp(): #getting highest temp from selected hours
    maxtemp = max(avgtemplist)
    timeindex = avgtemplist.index(maxtemp)
    print(f"Highest temperature: {maxtemp}C at hour: {timeindex + 1}") #{timeindex + 1} since index starts from 0.

exitprog = False
while exitprog == False:
    selectoption = input('''====================================
    Please choose option:
    a - List of Temperature Data
    b - Average Temperature Calculator
    q - Exit Program
    ====================================''')
    if selectoption.lower() == "a":
        for i, ix in enumerate(temp): #i, ix is index, value
            print(f"Hour:{i+1} Temperature:{ix}")
    elif selectoption.lower() == "b":
        start = int(input("Please enter starting hour: "))
        end = int(input("Please enter ending hour: "))
        print(nhouravgTemp(start, end))
        print(maxnTemp())
        exitprog = True
    elif selectoption.lower() == "q":
        print("Goodbye.")
        exitprog = True
    else:
        selectoption = input("Invalid input. Please try again.")