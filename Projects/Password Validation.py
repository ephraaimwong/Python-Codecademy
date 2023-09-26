#first prompt outside the while loop so that it only prompts once
userpass = input('''Please enter desired password:
*Password should contain 1 uppercase, 1 lowercase, 1 special character and be at least 8-15 characters*
''')
passvalidity = False
while passvalidity == False:

    testpass = []
    #if using split() method, there will be 'list has no attribute' error
    for i in userpass: 
        testpass.append(i)

    uppercheck = 0
    lowercheck = 0
    digitcheck = 0
    specialchar = 0
    lengthcheck = 0

    #check len() first before it splits
    if 15>= len(userpass) >= 8: 
        lengthcheck += 1 
        for i in testpass:
            if i.isupper():
                uppercheck += 1
            if i.islower():
                lowercheck += 1
            if i.isdigit():
                digitcheck += 1
            if i is not i.isalnum(): #.isalnum checks for alphabets AND numbers 
                specialchar += 1

    if (uppercheck >= 1 and lowercheck >= 1 and digitcheck >= 1 and specialchar >= 1 and lengthcheck >= 1):
        print("Valid password")
        passvalidity = True
    else:
        userpass = input('''
Password should contain 1 uppercase, 1 lowercase, 1 special character and be at least 8-15 characters. 
Please try again.
''')
