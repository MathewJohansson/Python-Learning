# While loop = repeated if statement

z = 6
if z % 2 == 0 : 
    print("z is divisible by 2") 
elif z % 3 == 0 : 
    print("z is divisible by 3") 
else :
    print("z is neither divisible by 2 nor by 3") 



# while condition :
#    expression

# Repeating action until condition is met

error = 50.0 

while error > 1 :
    error = error / 4
    print(error)



# For loops

for var in seq : 
    expression 

# "for each var in seq, exec expression"abs

fam = [1.73, 1.68, 1.71, 1.89]

for height in fam :
    print(height) 

# Display index in list
for index, height in enumerate(fam) :
    print("index " + str(index) + ": " + str(height))

# Increase index by one with each iteration
for index, area in enumerate(fam) :
    print("room " + str(index + 1) + ": " + str(fam))



# Loop over a string

for c in "family" :
    print(c.capitalize())



# Another example 

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
         
for x, y in house :
    print("the " + str(x) + " is " + str(y) + " sqm")



# Dictionaries 

world = { "afghanistan":30.55,
          "albania":2.77,
          "algeria":39.21 }

for key, value in world : 
    print(key + " -- " + str(value))

# To generate a key and value for each iteration
for x, y in world.items() :
    print(key + " -- " + str(value))



# Looping through 2D NumPy arrays

import numpy as np 
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
meas = np.array([np_height, np_weight])
for val in meas : 
    print(val)

# To print each element of the array 
for val in np.nditer(meas) :
    print(val) 



# Quick recap:

# For dictionary, use key, val in my_dict.items() :
# Dictionaries require a method

# For NumPy array, use for val in np.nditer(my_array) :
# NumPy arrays use a function 



# Looping with a Pandas DataFrame 

import pandas as pd 
brics = pd.read_csv("brics.csv", index_col = 0) 
for lab, row in brics.iterrows() :
    print(lab)
    print(row) 

# Print out label and capital on each iteration 
for lab, row in brics.iterrows() : 
    print(lab + ": " + row["capital"]) 

# Adding new col with length of country names 
for lab, row in brics.iterrows() : 
    brics.loc[lab, "name_length"] = len(row["country"])
print(brics)

# Adding new col with names of countries in upper case 
for lab, row in brics.iterrows() : 
    brics.loc[lab, "COUNTRY"] = row['country'].upper()
print(brics)

# Another way of writing that 
for lab, row in brics.iterrows() :
    brics.loc[lab, "COUNTRY"] = str.upper(row["country"])



# Calculate an entire DataFrame col by applying a function on a
#   particular col in an element-wise fashion (a better way)

brics["name_length"] = brics["country"].apply(len)
# much more efficient! 

