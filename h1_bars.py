# -*- coding: utf-8 -*-
"""
CS 592 HW 1 Plot 1
Created on Fri Jan 21 09:56:04 2022

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

us_mpg, japan_mpg, europe_mpg = [], [], []

# assign each mpg to a different list based on corresponding place of origin
for i in range(0,len(org)):
    if org[i] == "US":
        us_mpg.append(mpg[i])
    elif org[i] == "Japan":
        japan_mpg.append(mpg[i])
    else:
        europe_mpg.append(mpg[i])

# turn mpgs for each country from strings into int for plotting
us_mpg = [float(i) for i in us_mpg]
japan_mpg = [float(i) for i in japan_mpg]
europe_mpg = [float(i) for i in europe_mpg]

# make 3D list for histogramming
allmpg = [us_mpg, japan_mpg, europe_mpg]

plt.figure(figsize=(12,4)) # adjust figure ratio
plt.grid('minor','both',zorder=0) # add grid lines in background

# histogram: bin from 0->51 in intervals of 3

plt.hist(allmpg, bins=range(0,51,3), histtype='bar', edgecolor="midnightblue",
         label=("US","Japan","Europe"),
         color=("gold","mediumvioletred","darkturquoise"), zorder=3)
"""
plt.hist(us_mpg, bins=range(0,51,3), histtype='bar', edgecolor="midnightblue",
         label="US",color="gold",zorder=3,rwidth=0.3)
plt.hist(japan_mpg, bins=range(0,51,3), histtype='bar', edgecolor="midnightblue",
         label="Japan",color="mediumvioletred",zorder=3,hatch="/",rwidth=0.3)
plt.hist(europe_mpg, bins=range(0,51,3), histtype='bar', edgecolor="midnightblue",
         label="Europe",color="darkturquoise",zorder=3,hatch="x",rwidth=0.3)
"""
# labels
plt.title("HW 1 Task 1")
plt.xlabel("Gas Mileage (mpg)")
plt.ylabel("Number of Car Models")

# set x axis limits and tick marks
plt.xlim([0, 51])
plt.xticks(np.arange(0, 51, 3.0))

plt.legend(title="Car Origin") # create legend

#plt.savefig("h1_bars.png",bbox_inches='tight',dpi=300) # save figure