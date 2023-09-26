from numpy import less


date = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rainfall = [13.2, 2, 4, 0.4, 4.8, 14.4, 9.6, 0, 5.6, 7.6]
total, average = 0, 0
his_avg = 9.5
for day, rain in zip(date, rainfall): #zip() pairs items in lists together by index
    print(f"Nov {day:2} rainfall is {rain:5.2f}mm.") #{day:2} & {rain:5} formats the position to be aligned when printing '''

for rfall in rainfall:
    total += rfall
    average = total / len(rainfall)
print(f"The 10 day average rainfall in November is {average:.2f}mm.") #{average:.2f} rounds average to 2 decimals (this only works on floats)

if average < his_avg:
    print("Lower than historical average.")
elif average > his_avg:
    print("Higher than historical average.") 