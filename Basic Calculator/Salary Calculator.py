payrate = int(input("Enter payrate($/hr): "))
workinghrs = int(input("Enter hours worked in the month: "))
#pay calculator
basesalary = workinghrs * payrate #Salary if no OT
if workinghrs > 160: #Salary if OT
    otpay = basesalary + ((workinghrs - 160) * basesalary * 1.50)
    print(f"Gross Salary: ${otpay:.2f}")
else:
    otpay = 0
    print(f"Gross Salary: ${basesalary:.2f}")

#tax and gross pay calculator
tax20 = 500*0.20
tax10 = 1000*0.10
if basesalary + otpay > 1500:
    tax = (basesalary + otpay - 1500) * 0.30
    print(f"Tax owed: ${tax + tax20 + tax10}")
    netpay = basesalary + otpay - tax - tax20 - tax10
    print(f"Net pay: ${netpay}")
elif 1001 < basesalary + otpay < 1500:
    tax = (basesalary + otpay - 1000) * 0.20
    print(f"Tax owed: ${tax + tax10}")
    netpay = basesalary + otpay - tax - tax10
    print(f"Net pay: ${netpay}")
elif basesalary + otpay < 1000:
    tax = (basesalary + otpay )* 0.10
    print(f"Tax owed: ${tax}")
    netpay = basesalary + otpay - tax
    print(f"Net pay: ${netpay}")

