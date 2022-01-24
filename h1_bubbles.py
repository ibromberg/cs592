# -*- coding: utf-8 -*-
"""
CS 592 HW 1 Plot 3
Created on Sun Jan 23 15:43:03 2022

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

# convert strings to floats
disp = [float(i) for i in disp]
mod = [float(i) for i in mod]
horse = [float(i) for i in horse]
mpg = [float(i) for i in mpg]

disp_norm = disp/np.max(disp)

#plot stuff
# gas mileage vs horsepower; color diff for years; size diff for disp

#plt.figure(figsize=(12,4)) # adjust figure ratio
plt.grid('minor','both',zorder=0) # add grid lines in background

#for i in range(0,5):
#    plt.scatter(allhorse[i],allmpg[i],s=alldispnorm[i]*2000,c=color[i],zorder=3)
    
plot = plt.scatter(horse,mpg,s=disp_norm*100,c=mod,cmap='viridis',edgecolor='navy',linewidth=0.5,zorder=3)

# labels
plt.title("HW 1 Task 3")
plt.xlabel("Horsepower (hp)")
plt.ylabel("Average Gase Mileage (mpg)")

# set x axis limits and tick marks
#plt.xlim([0, 51])
#plt.xticks(np.arange(70, 83, 1.0))

yrs = ["1970","1972","1974","1977", "1979", "1981"]

plt.legend(yrs, title="Year", loc='lower right') # create legend
#plt.legend(loc='upper right', title="Displacement")

plt.savefig("h1_bubbles.png",bbox_inches='tight',dpi=300) # save figure