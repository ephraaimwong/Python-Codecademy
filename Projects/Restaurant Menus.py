from datetime import *
now = datetime.now().time()

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

    def __repr__(self):
        return self.name

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        for menu in self.menus:
            if time >= menu.start_time and time < menu.end_time:
                print(menu)

class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return (f"{self.name} is available from {self.start_time} to {self.end_time}")

    def show_menu(self):
        print(f"{self.name}\n" + "="*54)
        for i in self.items:
            print(f"{i:48} ${self.items[i]:.2f}")

    def order_items(self):
        ordering = True
        self.bill_list = []
        while ordering == True:
            self.purchased_items = input("Enter Order: ").lower()
            if self.purchased_items in self.items:
                self.bill_list.append(self.purchased_items)
                fin_order = input("Finished with the order? Yes/No ")
                if fin_order.lower() == "yes":
                    ordering = False
                else:
                    continue
            else:
                print("That is not a menu item.")
                continue
        print(self.bill_list)

    def cal_bill(self):
        self.total = 0
        for i in self.bill_list:
            self.total += self.items[i]
            print(i)
        return(f"Total: ${self.total:.2f}")

#creating menus
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch_menu = Menu("Brunch Menu", brunch_items, time(11,00,00) , time(16,00,00))
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu("Early Bird Dinner Menu", early_bird_items, time(15,00,00), time(18,00,00))
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu("Dinner Menu", dinner_items, time(17,00,00), time(23,00,00))
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu("Kids Menu", kids_items, time(11,00,00), time(21,00,00))

#current franchises
#menus list to store the multiple menus
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]
flagship_store = Franchise("1232 West East End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

#creating new franchise
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Arepas Menu", arepas_items, time(10,00,00), time(20,00,00))
#arepas_menu MUST be a list since the above franchises are lists
arepas_store = Franchise("189 Fitzgerald Avenue", [arepas_menu])

#creating new business
take_a_arepa = Business("Take a' Arepa", [arepas_store])

print(arepas_menu.show_menu())
