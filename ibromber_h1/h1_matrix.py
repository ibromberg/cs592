# -*- coding: utf-8 -*-
"""
CS 592 HW 1 Plot 4
Created on Sun Jan 23 17:17:56 2022

@author: ilana
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
    cyl.append(input[i][2])
    disp.append(input[i][3])
    horse.append(input[i][4])
    weight.append(input[i][5])
    accel.append(input[i][6])
    mod.append(input[i][7])
    org.append(input[i][8])

mpg = [float(i) for i in mpg]
cyl = [float(i) for i in cyl]
disp = [float(i) for i in disp]
horse = [float(i) for i in horse]
weight = [float(i) for i in weight]
accel = [float(i) for i in accel]
mod = [float(i) for i in mod]

countrycolor = []
for i in range(0,len(org)):
    if org[i]=='US':
        countrycolor.append('mediumvioletred')
    elif org[i]=="Europe":
        countrycolor.append('darkturquoise')
    else:
        countrycolor.append('goldenrod')

size = 5
colors = 'Set1'
plt.figure(figsize=(12,12)) # adjust figure ratio

# --------------- row 1
plt.subplot(4,4,1)
plt.scatter(mpg,mpg,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks(np.arange(0, 41, 20))
plt.ylabel("MPG",fontsize=12,fontweight='bold')
plt.title("mpg")

plt.subplot(4,4,2)
plt.scatter(weight,mpg,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])
plt.title("lbs")

plt.subplot(4,4,3)
plt.scatter(horse,mpg,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])
plt.title("hp")

plt.subplot(4,4,4)
plt.scatter(disp,mpg,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])
plt.title("L")
plt.ylabel("mpg",labelpad=-170,rotation=360, fontsize=12)

# --------------- row 2 
plt.subplot(4,4,5)
plt.scatter(mpg,weight,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks(np.arange(2000, 5001, 1000))
plt.ylabel("Weight",fontsize=12,fontweight='bold')

plt.subplot(4,4,6)
plt.scatter(weight,weight,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,7)
plt.scatter(horse,weight,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,8)
plt.scatter(disp,weight,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])
plt.ylabel("lbs",labelpad=-170,rotation=360, fontsize=12)

# --------------- row 3
plt.subplot(4,4,9)
plt.scatter(mpg,horse,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks(np.arange(0, 201, 100))
plt.ylabel("Horsepower",fontsize=12,fontweight='bold')

plt.subplot(4,4,10)
plt.scatter(weight,horse,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,11)
plt.scatter(horse,horse,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])

plt.subplot(4,4,12)
plt.scatter(disp,horse,c=countrycolor,cmap=colors,s=size)
plt.xticks([])
plt.yticks([])
plt.ylabel("hp",labelpad=-170,rotation=360, fontsize=12)

# --------------- row 4
plt.subplot(4,4,13)
plt.scatter(mpg,disp,c=countrycolor,cmap=colors,s=size)
plt.xticks([0,50,25])
plt.yticks(np.arange(0, 401, 200))
plt.ylabel("Displacement",fontsize=12,fontweight='bold')
plt.xlabel("MPG",fontsize=12,fontweight='bold')

plt.subplot(4,4,14)
plt.scatter(weight,disp,c=countrycolor,cmap=colors,s=size)
plt.xticks(np.arange(2000,4001,2000))
plt.yticks([])
plt.xlabel("Weight",fontsize=12,fontweight='bold')

plt.subplot(4,4,15)
plt.scatter(horse,disp,c=countrycolor,cmap=colors,s=size)
plt.xticks(np.arange(0,201,200))
plt.yticks([])
plt.xlabel("Horsepower",fontsize=12,fontweight='bold')

plt.subplot(4,4,16)
plt.scatter(disp,disp,c=countrycolor,cmap=colors,s=size)
plt.xticks(np.arange(0,401,200))
plt.yticks([])
plt.xlabel("Displacement",fontsize=12,fontweight='bold')
plt.ylabel("L",labelpad=-170,rotation=360, fontsize=12)

#plt.grid('minor','both',zorder=0) # add grid lines in background

plt.savefig("h1_matrix.png",bbox_inches='tight',dpi=300) # save figure