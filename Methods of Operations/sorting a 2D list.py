toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
menu = []
for i, ix in zip(toppings, prices):
    menu.append([i, ix])
print(menu)
#.sort(key=lambda x:x[1]) will sort menu by 2nd element in sublist - prices.
menu.sort(key = lambda x:x[1])
print(menu)
