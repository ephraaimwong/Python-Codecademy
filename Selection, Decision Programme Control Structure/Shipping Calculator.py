exitprog = "no"
while exitprog.lower() == "no":
    
    inputans = "no"
    while inputans.lower() == "no":
        prod_price = input("Enter product price:")
        ship_weight = input("Enter shipment weight:")
        print("Product price:", prod_price, "Shipment weight:", ship_weight)
        inputans = input("Continue?")
#This class conversion is necessary for concatenation calculation on line 21
    ship_weight = float(ship_weight)
    prod_price = float(prod_price)

    if ship_weight <= 20:
        ship_cost = ship_weight * 2.50
    elif ship_weight in range(21 - 50):
        ship_cost = (20 * 0.50) + (ship_weight - 20) * 1.75
    else:
        ship_cost = ship_weight * 2.15

    total_price = prod_price + ship_cost
    print("Total price including shipping:", round(total_price,2))
    
    exitprog = input("Exit program?")