# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

''' 
Yr2 Astro Lab - Exoplanet Analysis: Transit identification
##########################################################

Good practices of Python:
1. Do NOT name variables with single letters unless it is an index; the name 
   should indicate its meaning or purpose.
2. Label indices and counters as i,j,k,n,m,l. 
3. Avoid hard-coding numbers into your code if possible - always express things 
   in terms of variables you already have inside the code. NEVER copy outputs 
   from the console back onto your script. 
4. Try to structure your code with functions - easier to fix if one goes wrong! 

'''

# Set the name of the datafile 
filename = 'Kep45.txt'

# For Data binning - set the number of sections 
num_sections = 2000

'''
The following code is given to start you off. 
Feel free to edit, remove or put them into functions. 


 - Data binning -

This code imports raw data from a file. data_x and data_y are the xy-coords of 
all original data points [Plotted in blue]. 

The code then smooths the lightcurve by diving the data into small sections. You 
may set the number of sections above.

In each section, we take a midpoint. We take the mean value in x (since they are
evenly spaced), and we take the median in y. If we then join these new points 
from all sections, we are effectively forming a 'fit curve' [Plotted in red]. 

binned_x and binned_y are arrays containing the x and y coords of this new fit
curve. You may now work with this new set of xy-coordinates to locate the transits. 


What is the purpose of doing data binning? When and why is this method useful? 
Discuss it in your notebook. 


## IMPORTANT ###
 Zoom in the plot and look at each individual transit. Does the shape of the 
 red curve at transits look approximately like a trapezium? Is the line between 
 tI and tII (or tIII and tIV) straight? Tweak the number of sections until it does. 
 
 What num_sections did you set? How would you use the smoothed curve to extract 
 the transit points?

 P.S. This step is not necessary if you are confident with your coding skills.
 However, you should soon realize that your code will be much simpler if every 
 large jump in gradient of the lightcurve contains only one section. 

'''

# Read the data file and extract the data from the two columns into 2 arrays 
data_x, data_y = np.loadtxt(filename, unpack=True)


# Data binning - Divides data array into small sections 
# you may tweak num_sections above 
splitted_x = np.array_split(data_x, num_sections)
splitted_y = np.array_split(data_y, num_sections)


# Initialize empty lists for storing outputs to be generated in the loop below 
binned_x = []
binned_y = []
# Loop through individual sections of x and y data 
for section_x, section_y in zip(splitted_x, splitted_y):
    # extract the x and y midpoint of each section 
    mid_x = np.mean(section_x)
    mid_y = np.median(section_y)
    # store the two midpoint outputs into the two lists  
    binned_x.append(mid_x)
    binned_y.append(mid_y)
# We now have a new set of xy-coords of the smoothed data (in red)


# Plot the raw data and the binned data 
fig1 = plt.figure(figsize=(16,6))
label = filename.replace('.txt', '')
ax1 = fig1.add_subplot(111)
ax1.set_title('{} Exoplanet Transit Lightcurve'.format(label))
ax1.set_xlabel('Time (Barycentric Julian Date)')
ax1.set_ylabel('Flux (e−/s)')
ax1.plot(data_x, data_y, '.', color='royalblue', markersize=1) 
ax1.plot(binned_x, binned_y,'-', color='red')
plt.show()


# You may now use the binned_x and binned_y array to find the transit points ---

###############################################################################



































