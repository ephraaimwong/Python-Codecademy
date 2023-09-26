from math import sqrt
landpricesqft = 25
landpricesqm = landpricesqft * 10.7639104
fencingpricem = 28.5
fencingpriceft = fencingpricem / 3.2808399

areatype = input("Feet or Meters?")
if areatype.lower() in ["sqft","feet","Feet"]:
    inputsqft = "no"
    while inputsqft == "no":
        areasqft = int(input("Enter the size of property:"))
        propertyvaluesqft = int(areasqft) * int(landpricesqft)
        print("Value of land is $", propertyvaluesqft, "for", areasqft, "sqft.")
        perimetersqft = sqrt(areasqft)
        quotedfencingpriceft = fencingpriceft * perimetersqft
        print("Price for fencing property is $", round(quotedfencingpriceft,2))
        inputsqft = input("Exit programme? Yes or No?")

elif areatype.lower() in ["m2", "meters", "Meters"]:
    inputsqm = "no"
    while inputsqm == "no":
        areasqm = int(input("Enter the size of property:"))
        propertyvaluesqm = int(areasqm) * int(landpricesqm)
        print("Value of land is $", propertyvaluesqm, "for", areasqm, "m2.")
        perimetersqm = sqrt(areasqm)
        quotedfencingpricem = fencingpricem * perimetersqm
        print("Price for fencing property is $", round(quotedfencingpricem,2))
        inputsqm = input("Exit programme? Yes or No?")