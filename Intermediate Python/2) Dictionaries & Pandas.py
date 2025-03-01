# Instead of lists (indexed by range of numbers): 
pop = [30.55, 2.77, 39.21]
countries = ["Afghanistan", "Albania", "Algeria"]
# Collection of values - order matters, for selecting entire subsets

# Use dictionaries (indexed by unique keys): 
world = {"Afghanistan":30.55, "Albania":2.77, "Algeria":39.21}
# Lookup table with unique keys

world["Albania"] # prints out 2.77



# Obtain country index; takes index of germany, prints same index
#       value in capitals list (berlin)
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

ind_ger = countries.index('germany')
print(capitals[ind_ger])



# Accessing dictionary

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo'}

# Prints keys then values of europe
print(europe.keys())
print(europe.values())

# Prints value that belongs to key 'norway'
print(europe['norway'])



# Delete key-value pair from world (not previously stated)
del(world["sealand"])

# Add key-value pair
europe['italy'] = 'rome'

# Update capital city (if bonn was first germany capital)
europe['germany'] = 'berlin' # now sets berlin as capital



# A dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Create sub-dictionary called data
data = { 'capital':'rome', 'population':59.83 }

# Add data to europe under key 'italy'
europe['italy'] = data



# Pandas - high-level data manipulation tool

# Dictionary into df
dict = {
    "country":["Brazil", "Russia", "India", "China", "South Africa"],
    "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area":[8.516, 17.10, 3.286, 9.597, 1.221],
    "population":[200.4, 143.5, 1252, 1357, 52.98]
}
import pandas as pd
brics = pd.DataFrame(dict)
brics 
brics.index = ["BR", "RU", "IN", "CH", "SA"]

# df from CSV file
brics.csv

# Save brics as csv file
# brics = pd.read_csv("path/to/brics.csv")

# Set first col is used as row labels (left of first col)
# brics = pd.read_csv("path/to/brics.csv", index_col = 0)

# Create a dictionary and add in pre-defined list
names = ['United States', 'Australia', 'Japan', 'India'] 
import pandas as pd
my_dict = { 'country':names } 
# can then set as dataframe: 
cars = pd.DataFrame(my_dict) 
print(cars)



# Pandas 2

#Square brackets:
# Col access
brics[["country", "capital"]]
# Row access - only through slicing
brics[1:4] 

# loc (label-based):
# Row access
brics.loc[["RU", "IN", "CH"]] 
# Col acces
brics.loc[:, ["country", "capital"]]
# Row and col access
brics.loc[
    ["RU", "IN", "CH"],
    ["country", "capital"]
]