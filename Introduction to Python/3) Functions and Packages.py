# Basic functions

var1 = [1, 2, 3, 4]
var2 = True
print(type(var1))
print(len(var1))

# Convert var2 into an integer
out2 = int(var2)

# Search for help
# ?max in Terminal



# Sorting/reverse sorting

# Lists
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)



# Methods 

fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
# Call method index() on fam to obtain that index (4)
fam.index("mom")

# Replace method
# sister.replace("z", "sa")
# In variable sister, letter z is replaced with letters sa

# fam.append("me") adds "me" onto end of fam


# String methods

# Upper-case
place = "poolhouse"
place_up = place.upper() 
print(place)
print(place_up) 

# Count number of o's in place
print(place.count('o'))

# Print index of element 20.0 from list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20.0))

# Reverse list
areas.reverse() 



# Packages

