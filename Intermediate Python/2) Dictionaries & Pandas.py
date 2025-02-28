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