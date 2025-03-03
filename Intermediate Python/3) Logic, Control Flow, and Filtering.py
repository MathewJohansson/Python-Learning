# Comparison operators - how two values relate, resulting in a boolean

import numpy as np 
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2
bmi

# Which comparisons are > 23? 
bmi > 23 # True on all comparisons

# bmi values > 23
bmi[bmi > 23] 

# Numbers and strings can be compared
# For comparing strings, these work alphabetically:
"carl" < "chris" # = True

# Comparing different types produces an error 



# and operator for multiple comparisons simultaneously
# Performing and on NumPy requires functions: 
logical_and()
logical_or()
logical_not()

# E.g.:
np.logical_and(bmi > 21, bmi < 22)



# If, elif, and else

# if condition :
#      expression

z = 4
if z % 2 == 0 :
    print("checking " + str(z))
    print("z is even")


z = 5
if z % 2 == 0 :
    print("z is even")
else: 
    print("z is odd")


z = 6
if z % 2 == 0 :
    print("z is divisible by 2") 
elif z % 3 == 0 :
    print("z is divisible by 3")
else :
    print("z is neither divisible by 2 or 3")



# Comparisons on element basis 

dict = {
    "country":["Brazil", "Russia", "India", "China", "South Africa"],
    "capital":["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area":[8.516, 17.10, 3.286, 9.597, 1.221],
    "population":[200.4, 143.5, 1252, 1357, 52.98]
}
import pandas as pd
brics = pd.DataFrame(dict)
brics

# Selecting countries with > 8 million km2
# 3 steps:
#   1. Select area col
#   2. Do comparison on area col
#   3. Use result to select countries

brics["area"]

# Bool results for > 8 mill km2
brics["area"] > 8

# All rows and cols for countries > 8
is_huge = brics["area"] > 8

# Country names > 8km2
brics[is_huge]

# Other way of typing this
brics[brics["area"] > 8]



# Bool operators on the above

# >8, <10
import numpy as np 
np.logical_and(brics["area"] > 8, brics["area"] < 10)

