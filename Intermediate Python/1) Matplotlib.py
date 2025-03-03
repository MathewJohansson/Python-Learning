# Control structures - necessary to customise the flow of scripts and algorithms. 

# Import, set arrays, basic x-y plot 
import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()

# Scatterplot
plt.scatter(year, pop)
plt.show()

# Plot on log scale, must follow a plot above (e.g., plt.scatter(..., ....))
plt.xscale('log')



# Histograms - give ideas on distributions

import matplotlib.pyplot as plt

# Help on histogram
help(plt.hist)

# Example
values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
plt.hist(values, bins = 3)
plt.show() 

# Cleans up the plot so you can start afresh
plt.clf()



# Labels - import, set arrays, plot, labels, then plt.show() 
plt.xlabel('Year')
plt.ylabel('POpulation')
plt.title('World Population Projections')
plt.yticks([0, 2, 4, 6, 8, 10],
           ['0B', '2B', '4B', '6B', '8B', '10B']) # Second list changes ylabel text for each interval
plt.show()

# Setting arrays as x-axis ticks
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']
plt.xticks(tick_val, tick_lab)

# Double size of plotted points (np_pop previously stated)
np_pop = np_pop * 2

# Specify c (colour for each) and alpha (transparency level)
plt.scatter(x = gdp_cap, 
            y = life_exp, 
            s = np.array(pop) * 2, 
            c = col, 
            alpha = 0.8)

# Additional plot customization
plt.text(1550, 71, 'India')

# Draw basic gridlines on plot
plt.grid(True)