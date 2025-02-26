# Create list 
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create then adapt list areas
areas = [hall, kit, liv, bed, bath]
print(areas)

areas = ["hallway", hall, "kitchen", kit, "living room", liv, "bedroom", bed, "bathroom", bath]
print(areas)

# List of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
        ["bedroom", bed],
        ["bathroom", bath]]

# Elements of a list
print(areas[5])
print(areas[-1])



# Slicing - First 6 items in areas list
downstairs = areas[:6]

# Slicing - Last 4 items/items from item 7 onwards
upstairs = areas[6:]



# Subset the house list (first item in house list of 1, last item in inner list)
house[-1][1]

# Manipulating list
areas[-1] = 10.50
print(areas)



# New list, additional 'room'
areas_1 = areas + ["poolhouse", 24.5]
print(areas_1)

# Delete poolhouse string and float (delete 10, float then becomes 10)
del areas_1[10]
del areas_1[10]
print(areas_1)



# Create copy of list, changes made don't affect original
areas_copy = areas[:] 