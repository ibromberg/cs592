# -*- coding: utf-8 -*-
"""
CS 592 HW 1 Plot 2
Created on Fri Jan 21 12:57:46 2022

@author: Ilana Bromberg
"""

import matplotlib.pyplot as plt
import numpy as np
import csv

# read in file
with open('cars.csv','r') as f:
    input = list(csv.reader(f,delimiter=";"))
del input[0:2] # trim off headings

# order of data:
# Car name (car); miles per gallon (mpg); number of cylinders (cyl); 
# Displacement (disp); Horsepower (horse); Weight; Acceleration (accel);
# Model year (mod); place of origin (org)

# create empty arrays
car,mpg,cyl,disp,horse,weight,accel,mod,org = [],[],[],[],[],[],[],[],[]

# split each input entry into lists for each value we're interested in
for i in range(0,len(input)): 
    car.append(input[i][0])
    mpg.append(input[i][1])
    cyl.append(input[i][2])
    disp.append(input[i][3])
    horse.append(input[i][4])
    weight.append(input[i][5])
    accel.append(input[i][6])
    mod.append(input[i][7])
    org.append(input[i][8])

# plot: avg gas mileage VS year for each country (three line plots)

us_mpg, japan_mpg, europe_mpg = [], [], []
us_yrs, japan_yrs, europe_yrs, yrs = [], [], [], []
us_mpg_avg, japan_mpg_avg, europe_mpg_avg = [], [], []

# assign each mpg to a different list based on corresponding place of origin
for i in range(0,len(org)):
    if org[i] == "US":
        us_mpg.append(mpg[i])
        us_yrs.append(mod[i])
    elif org[i] == "Japan":
        japan_mpg.append(mpg[i])
        japan_yrs.append(mod[i])
    else:
        europe_mpg.append(mpg[i])
        europe_yrs.append(mod[i])

# turn values for each country from strings into int for plotting
us_mpg = [float(i) for i in us_mpg]
japan_mpg = [float(i) for i in japan_mpg]
europe_mpg = [float(i) for i in europe_mpg]

us_yrs = [float(i) for i in us_yrs]
japan_yrs = [float(i) for i in japan_yrs]
europe_yrs = [float(i) for i in europe_yrs]

# create dictionaries
us_dict = {}
for i in range(len(us_yrs)):
    if not us_yrs[i] in us_dict.keys():
        us_dict[us_yrs[i]] = [us_mpg[i]] # make new list w corresponding mpg
    else:
        us_dict[us_yrs[i]].append(us_mpg[i]) # add mpg value to existing year list
        
japan_dict = {}
for i in range(len(japan_yrs)):
    if not japan_yrs[i] in japan_dict.keys():
        japan_dict[japan_yrs[i]] = [japan_mpg[i]] # make new list w corresponding mpg
    else:
        japan_dict[japan_yrs[i]].append(japan_mpg[i]) # add mpg value to existing year list
        
europe_dict = {}
for i in range(len(europe_yrs)):
    if not europe_yrs[i] in europe_dict.keys():
        europe_dict[europe_yrs[i]] = [europe_mpg[i]] # make new list w corresponding mpg
    else:
        europe_dict[europe_yrs[i]].append(europe_mpg[i]) # add mpg value to existing year list

# do averages for each year        
for key in us_dict.keys():
    us_mpg_avg.append(np.mean(us_dict[key]))
for key in japan_dict.keys():
    japan_mpg_avg.append(np.mean(japan_dict[key]))
for key in europe_dict.keys():
    europe_mpg_avg.append(np.mean(europe_dict[key]))
    
# remove duplicate years from year lists for plotting
[yrs.append(i) for i in us_yrs if i not in yrs]

#plot stuff
plt.figure(figsize=(12,4)) # adjust figure ratio
plt.grid('minor','both',zorder=0) # add grid lines in background

plt.plot(yrs,us_mpg_avg,color="gold",marker="o",label="US", zorder = 3)
plt.plot(yrs,japan_mpg_avg,color="mediumvioletred",marker="v",label="Japan", zorder = 3)
plt.plot(yrs,europe_mpg_avg,color="darkturquoise",marker="s",label="Europe", zorder = 3)

# labels
plt.title("HW 1 Task 2")
plt.xlabel("Year")
plt.ylabel("Average Gase Mileage (mpg)")

# set x axis limits and tick marks
#plt.xlim([0, 51])
plt.xticks(np.arange(70, 83, 1.0))

plt.legend(title="Car Origin") # create legend

plt.savefig("h1_lines.png",bbox_inches='tight',dpi=300) # save figure