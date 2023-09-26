from numpy import sin, single


brewed_price = {
    "small": 4.00,
    "medium": 4.75,
    "large": 5.50
    }
mocha_price = {
    "small": 4.25,
    "medium": 5.75,
    "large": 6.50
    }
latte_price = {
    "small": 4.50,
    "medium": 6.00,
    "large": 7.00
    }
extramilk_price = {
    "almond milk": 0.50,
    "soy milk": 0.50,
    "oat milk": 1.00,
    "none": 0.00
    }
menu = {
    "brewed coffee": brewed_price, "mocha": mocha_price, "latte": latte_price, "milk": extramilk_price
    }

def coffeebot():
    print("Welcome to the Cafe!")
    orderloop = True
    bill = 0
    orderlist = []
    while orderloop == True:
        drink_size = get_size()
        drink_type = get_drink()
        add_on = extramilk()
        #orderlist to store the ongoing orders
        orderlist.append(joinstr(drink_type.lower(), drink_size.lower(), add_on.lower()))
        if "Latte" in drink_type:
            drink_type = "latte" #changing to "latte" if latte variations are ordered so it can look up menu{} 
        #total is temp variable, bill is running balance while still ordering
        total = calculate_bill(drink_type.lower(), drink_size.lower(), add_on.lower())
        bill += total

        orderprompt = input("Finish order? Yes/No \n")
        if orderprompt.lower() == "yes":
            orderloop = False
    username = input("Can I get a name please? \n")
    if len(orderlist) == 1:
        #removes printing of list format 
        for i in orderlist:
            singleorder = i.title()
        if add_on == "none":
            singleorder = singleorder[:-5] #removes printing "none" for no add ons
            print(f"Thank you {username}!\nYour {singleorder} will be ready shortly.\nTotal comes down to ${bill:.2f}")
        else:
            print(f"Thank you {username}! Your {singleorder} will be ready shortly.\nTotal comes down to ${bill:.2f}")
    else:
        print(f"Thank you {username}! The following orders will be ready shortly: \n")
        for i, ix in enumerate(orderlist): #enumerate() so that the list of orders will be numbered
            print(f"{i+1} - {ix.title()}\n")
        print(f"Total comes down to ${bill:.2f}")

def joinstr(drink, size, add_on): #joinstr() to join full drink order as 1 item to append in orderlist
    joinstring = []
    joinstring.append(size)
    joinstring.append(drink)
    joinstring.append(f"/ additional {add_on}")
    order = " ".join(joinstring)
    return order

def calculate_bill(drink, size, add_on):
    total = 0
    total += menu[drink][size] #to access price from dict in dict
    total += menu["milk"][add_on]
    return total

def get_size():
    orderloop = True
    while orderloop == True:
        usersize = input("What size drink can I get for you? \na - Small \nb - Medium \nc - Large \n")
        if usersize.lower() == "a" or usersize == "small":
            orderloop = False
            usersize = "small"
            return usersize.title()
        elif usersize.lower() == "b" or usersize == "medium": 
            orderloop = False
            usersize = "medium"
            return usersize.title()
        elif usersize.lower() == "c" or usersize == "large":
            orderloop = False
            usersize = "large"
            return usersize.title()
        else:
            print("Invalid input.")
    
def get_drink():
    orderloop = True
    while orderloop == True:
        userdrink = input("What type of drink would you like? \na - Brewed Coffee \nb - Mocha \nc - Latte \n")
        if userdrink.lower() == "a" or userdrink == "brewed coffee":
            orderloop = False
            userdrink = "Brewed Coffee"
            return userdrink
        elif userdrink.lower() == "b" or userdrink == "mocha": 
            orderloop = False
            userdrink = "Mocha"  
            return userdrink
        elif userdrink.lower() == "c" or userdrink == "latte":
            orderloop = False
            lattemilk = order_latte()
            userdrink = "Latte"
            return (f"{userdrink} with {lattemilk}")
        else:
            print("Invalid input.")


def order_latte():
    orderloop = True
    while orderloop == True:
        usermilk = str(input("What milk would you prefer? \na - 2% Milk \nb - Non-Fat Milk \nc - Soy Milk \n"))
        if usermilk.lower() == "a" or usermilk == "2% milk":
            orderloop = False
            usermilk = "2% Milk"
            return usermilk
        elif usermilk.lower() == "b" or usermilk == "non-fat milk": 
            orderloop = False
            usermilk = "Non-Fat Milk"
            return usermilk
        elif usermilk.lower() == "c" or usermilk == "soy milk":
            orderloop = False
            usermilk = "soy milk"
            return usermilk
        else:
            print("Invalid input.")

def extramilk():
    orderloop = True
    while orderloop == True:
        extramilk = input("Would you like any special additions? \na - Almond Milk \nb - Soy Milk \nc - Oat Milk \nd - None\n")
        if extramilk.lower() == "a" or extramilk == "almond milk":
            orderloop = False
            extramilk = "Almond Milk"
            return extramilk
        elif extramilk.lower() == "b" or extramilk == "soy milk":
            orderloop = False
            extramilk = "Soy Milk"
            return extramilk
        elif extramilk.lower() == "c" or extramilk == "oat milk":
            orderloop = False
            extramilk = "Oat Milk"
            return extramilk
        elif extramilk.lower() == "d" or extramilk == "none":
            orderloop = False
            extramilk = "none"
            return extramilk
        else:
            print("Invalid input.")


            
# print(menu)
# print(menu["mocha"])
# print (menu["mocha"]["small"])
coffeebot()

