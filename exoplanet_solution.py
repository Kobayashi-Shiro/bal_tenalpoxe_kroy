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
num_sections = 1107   ### start with 2000 for student ver 

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



''' Solution and Notes for demonstrator '''

'''
 Skills required to complete this lab: 

 1. for-loops, used along with range(), or can opt for while-loops 
 2. making use of indicies in arrays/lists 
 3. using lists to store outputs from each iteration of a loop; append()
    [not done in yr1, will have to teach this]
 4. basic numpy tools 
 
 Note I have not used a lot of numpy tools in this solution when doing operations, 
 since in first year they were taught to do things manually. Maybe that helps to
 better understand what's going on inside. 
 
'''

'''
 ———————————————————————— Tasks for 1st lab section ———————————————————————————
 
 Workshop style - Let them choose data from exoplanet archive and import data 
 themselves (should have done it in Yr1 Lab6). Plot the raw lightcurve. 
 
 Allow 1 hr or so to discuss and think about the algorithm. Data contains lots 
 of noise, how can it be 'removed', what do we need to do to allow the four points 
 to be precisely extracted. KEY: How to plan an algorithm. 
 
 If some managed to do it, go ahead. For the rest, send the starting code. 

 1. Look at the plotted graphs and change the number of sections such that the 
    new xy plots can form trapeziums and locate the required transit points. 
    Make sure they understand importance of doing data binning 

 2. Write a code to extract sections with large increase/decrease, then test 
    code with different filtering limits 
    
 3. Extract the time and flux (x and y) of the four points using indicies. Append
    them to lists. 

'''
tI_list = []
tII_list = []
tIII_list = []
tIV_list = []

fI_list = []
fII_list = []
fIII_list = []
fIV_list = []

# loop through each section 
for i in range(len(binned_y)-1):    
    # gradient 
    grad = (binned_y[i+1] - binned_y[i]) / (binned_x[i+1] - binned_x[i])

    # Transit start 
    if grad < -3800:  ### Tweak this; should be the only bit that needs hard-coding 
        
        # directly extract the two points connecting to this section
        tI = binned_x[i]
        tII = binned_x[i+1]
        fI = binned_y[i]
        fII = binned_y[i+1]   
        
        # learn how to append to lists 
        tI_list.append(tI)
        tII_list.append(tII)
        fI_list.append(fI)
        fII_list.append(fII)
    
    # Transit end 
    elif grad > 4080:  ### Tweak this 
        
        # same, maybe draw a diagram to help understanding 
        tIII = binned_x[i]
        tIV = binned_x[i+1]
        fIII = binned_y[i]
        fIV = binned_y[i+1]
        
        tIII_list.append(tIII)
        tIV_list.append(tIV)
        fIII_list.append(fIII)
        fIV_list.append(fIV)

#### IMPORTANT ####
# Before they proceed, make sure both the number of transit start and end 
# points matches the number of transits on the graph 
# If the numbers do not match, change the num_sections and/or gradient filters

print('Number of downs:',len(tI_list))
print('Number of ups',len(tIII_list))


# [Optional] Plot the transit points onto the graph 
transit_x = tI_list + tII_list + tIII_list + tIV_list 
transit_y = fI_list + fII_list + fIII_list + fIV_list 
ax1.plot(transit_x, transit_y, 'o', color='orange')


# Transit midpoints 
mid_t_list = []
for i in range(len(tI_list)):
    # get mid with tI and tIV
    mid_I_IV = (tIV_list[i] + tI_list[i])/2.
    # get mid with tII and tIII
    mid_II_III = (tIII_list[i] + tII_list[i])/2.
    # take avg 
    mid_t_list.append(np.mean([mid_I_IV, mid_II_III]))


# Print all and check if the numbers are sensible before proceeding 
print('tI_list:\n', tI_list)
print('tII_list:\n', tII_list)
print('tIII_list:\n', tIII_list)
print('tIV_list:\n', tIV_list)
print('mid_t_list:\n', mid_t_list)
    

'''
 ——————————————————————— Tasks for 1st/2nd lab section ————————————————————————

 Most should be able to independently carry on finding the physical properties 
 after the above step. 
 
 4. Finding the Orbital Period  
 
'''
period_list = []
for i in range(len(mid_t_list)-1):
    # taking difference between each mid_t
    period = mid_t_list[i+1] - mid_t_list[i]
    period_list.append(period)

# Mean orbital period 
orb_period = np.mean(period_list)
# Standard error of mean 
orb_period_err = np.std(period_list) / np.sqrt(len(period_list))

print('Orbital period: ({} +/- {}) days'.format(round(orb_period,3),  \
                                                round(orb_period_err, 3)))


''' 5. Calculate (delF/F) term and error '''

delF_F_list = []
for i in range(len(fI_list)):
    # get del_F/F with I and II
    delF_F_I_II = (fI_list[i] - fII_list[i]) / fI_list[i]
    # get del_F/F with III and IV 
    delF_F_III_IV = (fIV_list[i] - fIII_list[i]) / fIV_list[i]
    # take the greater one, or mean is okay 
    # (considering the fact that some of them detected a point in the middle)
    delF_F_list.append(max(delF_F_I_II, delF_F_III_IV))
delF_F = np.mean(delF_F_list)
delF_F_err = np.std(delF_F_list) / np.sqrt(len(delF_F_list))
    
print('del_F/F: ({} +/- {})'.format(round(delF_F,3), round(delF_F_err, 3)))



''' 6. Calculate (tT^2 - tF^2) term and error '''

tT2_tF2_list = []
for i in range(len(tI_list)):
    tT2 = (tIV_list[i] - tI_list[i])**2
    tF2 = (tIII_list[i] - tII_list[i])**2
    tT2_tF2_list.append(tT2 - tF2)
tT2_tF2 = np.mean(tT2_tF2_list)
tT2_tF2_err = np.std(tT2_tF2_list) / np.sqrt(len(tT2_tF2_list))

print('tT^2 - tF^2: ({:.2E} +/- {:.2E}) days^2'.format(tT2_tF2, tT2_tF2_err))


'''
 ————————————————————————— Tasks for 2nd lab section ——————————————————————————
 
 Find the physical properties of the exoplanet.

 7. Calculate the Radius of planet 
 
'''
star_radius = 1.3 * 6.955e8  # m

planet_radius = np.sqrt(delF_F) * star_radius
# by error propagation 
planet_radius_err = 1/2 * delF_F_err/delF_F * planet_radius

print('Planet radius: ({:.2E} +/- {:.2E}) m'.format(planet_radius, planet_radius_err))



''' 8. Calculate Planet velocity '''

# numerator and denominator of V_p formula 
numer = 4 * delF_F**(1/4)
denom = (tT2_tF2)**(1/2)

planet_vel = numer / denom * star_radius  # m/days   
# by error propagation 
numer_err = 1/4 * delF_F_err/delF_F * numer 
denom_err = 1/2 * tT2_tF2_err/tT2_tF2 * denom 
planet_vel_err = np.sqrt((numer_err/numer)**2 + (denom_err/denom)**2) * planet_vel 

# convert units - m/days to m/s 
planet_vel = planet_vel / (24*60*60)
planet_vel_err = planet_vel_err / (24*60*60)

print('Planet velocity: ({:.2E} +/- {:.2E}) m/s'.format(planet_vel, planet_vel_err))



'''
 [SOLUTION] Results from literature (Exoplanet archive): 

 Orbital Period: 2.45 days 	
 Planet radius: 10.76±1.23 earth radii -> 6.86E+07 m 
 Planet semi-major axis: 0.03 AU 
 Planet velocity approx. = 2pi * semimajor axis / orbital period = 1.33E+05 m/s
 
 Main source of error: Smoothing of lightcurve during data binning, causes 
 errors in locating the four points. But this is more complicated to do hence 
 it's beyond scope of lab work.  
 
'''


''' 
 9. [Optional] Stacking multiple transits 
 Align transit dips with their midpoints, taking their fI or fIV into account 
 
'''

stacked_x = []
stacked_y = []

# loop through each transit 
for i, midpt in enumerate(mid_t_list):
    
    # cut out a section of data around each transit
    cut_min = midpt - 0.1 
    cut_max = midpt + 0.1 
    
    # normal flux (fI or fIV) at this transit 
    norm_flux = max([fI_list[i], fIV_list[i]])
    # set first normal flux as ref point for the rest 
    if i == 0:
        ref_flux = norm_flux 
    
    for raw_x, raw_y in zip(data_x, data_y):
        if raw_x >= cut_min and raw_x < cut_max:
            
            # shift the set of x data around each transit to the 1st one
            raw_x_shifted = raw_x - i * orb_period
            
            # normalize the corresponding y to the ref point 
            raw_y_shifted = raw_y - (norm_flux - ref_flux)
            
            stacked_x.append(raw_x_shifted)
            stacked_y.append(raw_y_shifted)

fig2 = plt.figure(figsize=(12,4))
ax2 = fig2.add_subplot(111)
ax2.set_title('{} Exoplanet Transit Stacked Lightcurve [Method 1]'.format(label))
ax2.set_xlabel('Time (Barycentric Julian Date)')
ax2.set_ylabel('Flux (e−/s)')
ax2.plot(stacked_x, stacked_y, '.', color='green', markersize=1) 
plt.show()




















