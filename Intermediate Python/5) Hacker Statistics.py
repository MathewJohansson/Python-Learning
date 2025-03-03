# Random generators 

import numpy as np 
np.random.rand()
np.random.seed(123)

# Randomly generate 0 or 1
coin = np.random.randint(0,2)
print(coin)

if coin == 0 : 
    print("heads")
else: 
    print("tails")



# Print random 

np.random.seed(123)
print(np.random.rand())



# Step simulation with dice 
# 1 or 2 on dice = step down/backwards
# 3, 4, or 5 on dice = step up/forwards
# 6 on dice = take turn again, move as many steps as next dice says

# Starting step 
step = 50

# Roll the dice 
dice = np.random.randint(1,7) 

# Finish the control construct
if dice <= 2 : 
    step = step - 1
elif dice <= 5 :
    step = step + 1
else : 
    step = step + np.random.randint(1,7)

# Print out dice and step 
print(dice, step)



# Random walk = series of random steps

# Iterations list; creates array of 10 outcomes 

import numpy as np 
np.random.seed(123)
outcomes = []
for x in range(10) :
    coin = np.random.randint(0, 2)
    if coin == 0 : 
        outcomes.append("heads")
    else :
        outcomes.append("tails")
print(outcomes)

# Tracking total number of tails 

import numpy as np 
np.random.seed(123)
tails = [0]
for x in range(10): 
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)

outcomes
tails



# Simulating a random walk 

import numpy as np 
np.random.seed(123) 

# Initialise random_walk
random_walk = [0]

# Complete the loop 
for x in range(100) :
    # Set step as last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step 
    if dice <= 2 :
        step = step - 1
    elif dice <= 5 : 
        step = step + 1
    else : 
        step = step + np.random.randint(1,7) 

    # Append next_step to random_walk
    random_walk.append(step)



# To make sure the steps don't go below 0

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)



# Plot random_walk 

import matplotlib.pyplot as plt 
plt.plot(random_walk)
plt.show()



# Distribution: 
# # After 100 steps, what is the distribution of outcomes if this 
#      is repeated 1000s of times? 

#  Back to total number of tails after 10 coin tosses:
import numpy as np 
np.random.seed(123) 
tails = [0]
for x in range(10) :
    coin = np.random.randint(0, 2)
    tails.append(tails[x] + coin)


# To find the distribution of this:

# 1. Set random seed, create empty list
import numpy as np 
np.random.seed(123)
final_tails = []

# 2. For loop that runs 10000 times 
for x in range(10000) : 
    tails = [0]
    for x in range(10) :
        coin = np.random.randint(0, 2)
        tails.append(tails[x] + coin)
    final_tails.append(tails[-1])
# 3. After simulating the first game, append the last number ^

# 4. Print number of tails for each 10 games (e.g., 4 = 4 tails out of 10)
print(final_tails)

# 5. The above is a set of distribution values that can be visualised
import matplotlib.pyplot as plt
plt.hist(final_tails, bins = 10) 
plt.show()



# Simulating multiple walks 

# NumPy is imported; seed is set

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk five times
for i in range(5) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)

# all_walks is a list of lists - every sub-list represents a single random walk.

# initialize and populate all_walks
all_walks = []
for i in range(20) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t 
np_aw_t = np.transpose(np_aw)
#         now every row in np_all_walks represents the position after 1 throw for the 500 random walks

# Plot np_aw_t
plt.plot(np_aw_t)
plt.show()



# Simulate random walk 500 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        if np.random.rand() <= 0.001 :
            step = 0
        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
plt.hist(ends)
plt.show()

