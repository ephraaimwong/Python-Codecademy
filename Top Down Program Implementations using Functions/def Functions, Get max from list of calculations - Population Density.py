region = [1, 2, 3, 4, 5]
area = [132.7, 93.1, 134.5, 103.9, 201.3]
pop = [922980, 686050, 573950, 921940, 921340]
popden = []
indexregion = 0
for a, p in zip(area, pop):
    density = (p / a)
    popden.append(density) #append density calculations to the popden list

def popDen():
    for r, d in zip(region, popden):   
        print(f"The population density of region {r} is {d:.2f}km2.")

def maxDen():
    maxden = 0
    maxden = max(popden) #gets highest value in popden list
    indexregion = popden.index(maxden) #gets index of highest value
    print(f"Region {indexregion} has the highest population density of {maxden:.2f}km2.")

print(popDen())
print(maxDen())