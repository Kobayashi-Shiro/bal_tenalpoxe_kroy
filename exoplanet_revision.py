# -*- coding: utf-8 -*-

'''
Yr2 Astro Lab - Exoplanet Analysis: Transit identification
##########################################################

 - Prerequisite -

This file contains the prior knowledge required for completing the exoplanet 
lab. Most should be revision (to refresh memory from first year) but some are 
new to them, such as lists and append(). 
Make sure this is avaible to the students before the lab and they are expected 
to have completed the mini exercise to gain the necessary skills. 

'''

import numpy as np

'''
##### 1. For-loops and indicies #####

In first year we have used for-loops to do some mathematical calculations. 
Recall Lab2 where we have used for-loop with the counter i to sum numbers
from 1 to 5. 
'''
ans1 = 0

for i in range(1,6,1):
    ans1 = ans1 + i
    
print(ans1)

'''
Then in Lab5 we have created a function which computes the integral of a given 
set of x and y data. Here, we used the counter i to specify a particular element 
in the x and y arrays. 
'''
def integrate(x, y):
    total = 0
    ith_result = 0
    
    # Loop through all x and y values in the arrays apart from the first one; 
    # we use len(x) to indicate the total number of elements in x array
    for i in range(1, len(x), 1): 
        # Calculates the area under the ith element of the curve 
        ith_result = y[i] * (x[i] - x[i-1])   
        total = total + ith_result   # This is the running sum

    # Return the final result after looping through all elements of x and y            
    return total 

# Create an array that spans from 0 to 4*pi with 100 divisions
x = np.linspace(0, 4 * np.pi, 100)  
# Create another array, y, that has the same number of elements as array x.     
y = np.exp(-0.25 * x) * np.cos(x)       

print(integrate(x, y))


'''
##### 2. Lists and append #####

Lists are very similar to arrays - a 1-D collection of ordered items. We create 
a list with  square brackets []. Again, we can access individual elements by 
specifying its index. 
'''
example_list1 = [2,4,6,8,10,12,14]
example_list2 = ['a','b','c','d','e']

print(example_list1[4])   # this gives 10 
print(example_list2[2])   # this gives c 


''' 
Lists are less convenient than arrays when it comes to numerical operations. For 
example, we can directly divide arrays by constants   
'''
x_array = np.array([1,2,3,4,5,6,7])
new_x_array = x_array / 10.
print(new_x_array)
'''
but for lists, if we do it the same way   
'''
# x_list = [1,2,3,4,5,6,7]
# new_x_list = x_list / 10.
# print(new_x_list)
'''
this will give an error. We will have to do 
'''
x_list = [1,2,3,4,5,6,7]
for x in x_list:
    new_x = x / 10. 
    print(new_x)
'''
Notice here we've only printed the output in each loop iteration. This makes 
it hard to continue the code for next step of calculation. We need a way to 
store all outputs into a single variable, such that it can be later accessed.  

Lists are useful for collecting outputs from each iteration into a single list. 
We use the append() method. 
'''

# First, we declare an empty list. 
# We let python know we are going to start a bucket and we will throw results in 
# afterwards.
new_x_list = []

# We are now ready to write the loop. Again 
for x in x_list:
    new_x = x / 10.     
    # we got the result. And we have to store it. We do -
    new_x_list.append(new_x)
    # so basically, 
    # <list for storing things>.append(<the thing you want to store>)

# We may then go outside the for-loop and retrieve the bucket (which is now filled)
print(new_x_list)



'''
Try the following mini-exercise:

We have two arrays of the same length. Calculate the difference between each 
consecutive element for each array, and store results to create two lists - let's 
call it diff1_list and diff2_list. 
Then, subtract each element in diff1_list by those in diff2_list,
if the result is less than 10, store it into a new list. 
Print your final result. 

'''
array1 = [45,63,67,98,12,34,53]
array2 = [7,21,38,95,63,14,64]


''' Solution '''

def element_diff(array):
    diff_list = []
    for i in range(len(array)-1):
        diff = array[i+1] - array[i]
        diff_list.append(diff)
    return diff_list

diff1_list = element_diff(array1)
diff2_list = element_diff(array2)

arr_diff_list = []
for i in range(len(diff1_list)):
    arr_diff = diff2_list[i] - diff1_list[i]
    if arr_diff < 10:
        arr_diff_list.append(arr_diff)

print(arr_diff_list)  # [-4, -71]
















