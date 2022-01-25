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
    #car.append(input[i][0])
    mpg.append(input[i][1])
    #cyl.append(input[i][2])
    disp.append(input[i][3])
    horse.append(input[i][4])
    #weight.append(input[i][5])
    #accel.append(input[i][6])
    mod.append(input[i][7])
    #org.append(input[i][8])

# convert strings to floats
disp = [float(i) for i in disp]
mod = [int(i) for i in mod]
horse = [float(i) for i in horse]
mpg = [float(i) for i in mpg]

mod = [i+1900 for i in mod]

# normalize size of displacement for plotting bubbles
disp_norm = disp/np.max(disp)
legend = [100*disp_norm,200*disp_norm,300*disp_norm]


#plt.figure(figsize=(12,4)) # adjust figure ratio
plt.grid('minor','both',zorder=0) # add grid lines in background
    
plt.scatter(horse,mpg,s=disp_norm*100,c=mod,cmap='viridis',
                   edgecolor='black',linewidth=0.5,zorder=3)
plt.colorbar(label="Years")

# single dots for legend, plotted outside of range of plot axes
plt.scatter(-100,-100,s=50*disp_norm,label="50 centiliter",c='navy',
            edgecolor='black',linewidth=0.5)
plt.scatter(-100,-100,s=150*disp_norm,label="150 centiliter",c='navy',
            edgecolor='black',linewidth=0.5)
plt.scatter(-100,-100,s=300*disp_norm,label="300 centiliter",c='navy',
            edgecolor='black',linewidth=0.5)

plt.xlim([-10, 250])
plt.ylim([-3,50])

# labels
plt.title("Car Characteristics between 1970 and 1982")
plt.xlabel("Horsepower (hp)")
plt.ylabel("Average Gase Mileage (mpg)")

# legends
plt.legend(loc='upper right', title="Displacement")

plt.savefig("h1_bubbles.png",bbox_inches='tight',dpi=300) # save figure