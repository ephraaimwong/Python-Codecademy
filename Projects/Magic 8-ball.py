"""
Magic 8-ball will answer a "yes/no" question with 9 different responses:
1. Yes - definitely.
2. It is decidedly so.
3. Without a doubt.
4. Reply hazy, try again.
5. Ask again later.
6. Better not tell you now.
7. My sources say no.
8. Outlook not so good.
9. Very doubtful.
"""
from random import randint
ballresponse = {
1: "Yes - definitely.",
2: "It is decidedly so.",
3: "Without a doubt.",
4: "Reply hazy, try again.",
5: "Ask again later.",
6: "Better not tell you now.",
7: "My sources say no.",
8: "Outlook not so good.",
9: "Very doubtful."
}
def userinput():
    name = input("Enter name: ")
    qns = input("Enter question: ")
    global qnsfilled 
    qnsfilled = True
    if len(name) == 0:
        print(f"Question: {qns}")
    else:
        print(f"{name} asks: {qns}")
    if len(qns) == 0:
        qnsfilled = False

        

def ballans():
    resnum = randint(1, len(ballresponse))
    ballans = ballresponse[resnum]
    if qnsfilled == True:
        print(f"Magic 8-Ball's answer: {ballans}")
    elif qnsfilled == False:
        print("Magic 8-Ball cannot answer a question yet asked.")
print(userinput())
print(ballans())

