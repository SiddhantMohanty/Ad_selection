#Upper Confidence bound
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#Importing the dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv') 

#Implementing UCB
N = 10000
d = 10
#Step1
number_of_selection = [0]*d #no. of different types of the same ad
sums_of_reward = [0]*d
ads_selected = []
total_reward = 0
#Step2
for n in range(0, N):
    ad = 0
    max_upper_bound = 0
    for i in range(0, d):
        if (number_of_selection[i] > 0):
            average_reward = sums_of_reward[i] / number_of_selection[i]
            delta_i = math.sqrt(3/2 * math.log(n + 1)/number_of_selection[i]) #confidence interval
            upper_bound = average_reward + delta_i
        else:
            upper_bound = 1e400
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
            ad = i 
    ads_selected.append(ad)
    number_of_selection[ad] = number_of_selection[ad] + 1
    reward = dataset.values[n,ad]
    sums_of_reward[ad] = sums_of_reward[ad]+ reward
    total_reward = total_reward + reward
    
#Visualising the result
plt.hist(ads_selected)
plt.title('Histogram of ads selections')
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()
        