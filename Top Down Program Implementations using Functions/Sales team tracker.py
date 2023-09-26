team = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sales = [11140, 12560, 17670, 20055, 18762, 23270, 24850, 11880, 16788, 20956]
target = int(input("Enter sales target: "))

def aboveTarget():
    targetcounter = 0
    for i, ix in enumerate(sales):
        if ix > target:
            targetcounter += 1
            print(f"Sale of staff {i+1} is {ix}, above target")
        elif ix < target:
            print(f"Sale of staff {i+1} is {ix}, below target")
    print(f"{targetcounter} met the target")
print(aboveTarget())