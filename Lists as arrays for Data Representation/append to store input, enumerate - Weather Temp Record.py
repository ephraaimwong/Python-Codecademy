msgprompt1 = "Temperature of"
msgprompt2 = "degC"
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
temptotal = 0
temp_data = []
for ik in range(0,7):
    temp_day = float(input(f"{msgprompt1} {days[ik]} is: ")) #temp_day is temp variable to store input to be appendiced to temp_data
    temp_data.append(temp_day) 
    temptotal += temp_day #must be inside loop to repeat adding to total

print('''
==============================
Temperature Records as follows
==============================
''')

for ix, temp in enumerate(temp_data): #enumerate prints back the register value and index in the list
    print(f"{msgprompt1} {days[ix]} is {temp}")

tempavg = temptotal / len(days) #len(days) is register as number of items in list i.e. 7
print("The average temperature for the week is", round(tempavg,2), "degC.")