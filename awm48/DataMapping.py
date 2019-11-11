# -*- coding: utf-8 -*-
"""
Created on Sun Nov 9 19:03:22 2019

@author: Alex Marshall
Project Work with Data Mapping
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

#Key words to search by
ASSAULT = "assault"
BURGLARY = "burglary"
ROBBERY = "robbery"
LACERNY = "lacerny"
DRUG = "drug"

#New York
NYCrimes = []
NYCrimesMonth2013 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
NYCrimesMonth2014 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
NYCrimesMonth2015 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
with open('C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\NewYorkCrimes.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if ASSAULT in row[9].lower():
            date = row[1]
            try:
                month = int(date[:2].replace("/",""))
            except:
                print(date)
            else:
                year = int(date[-4:])
                if year == 2014 | year == 2015:
                    NYCrimesMonth2014[month] = NYCrimesMonth2014[month] + 1
                NYCrimesMonth2015[month] = NYCrimesMonth2015[month] + 1

data = NYCrimesMonth2014[1:13]
print(data)
bars = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec') 
y_pos = np.arange(len(bars))      
plt.bar(bars, data)
plt.title(label = 'Crimes per month in LA')
plt.xticks(y_pos, bars)
plt.show()

#San Francisco
SFCrimes = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes13 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes14 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes15 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes16 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes17 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes18 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
SFCrimes19 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
with open('C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\SanFranciscoCrimes.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if ASSAULT in row[14].lower():
            date = row[1]
            try:
                month = int(date[5:-3].replace("/",""))
                year = int(date[:4])
            except:
                print("d: ", date)
            else:
#                print("M: ", month)
#                print("Y: ", year)
                if year == 2013:
                    SFCrimes13[month] = SFCrimes13[month] + 1
                if year == 2014:
                    SFCrimes14[month] = SFCrimes14[month] + 1
                if year == 2015:
                    SFCrimes15[month] = SFCrimes15[month] + 1
                if year == 2016:
                    SFCrimes16[month] = SFCrimes16[month] + 1
                if year == 2017:
                    SFCrimes17[month] = SFCrimes17[month] + 1
                if year == 2018:
                    SFCrimes18[month] = SFCrimes18[month] + 1
                if year == 2019:
                    SFCrimes19[month] = SFCrimes19[month] + 1
                SFCrimes[month] = SFCrimes[month] + 1
 
sfdata = SFCrimes19[1:13]
print(sfdata)  
bars = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec') 
y_pos = np.arange(len(bars))     
plt.bar(bars, sfdata)
plt.title(label = 'Crimes per month in SF')
plt.xticks(y_pos, bars)
plt.show()

#Los Angeles     
LACrimes = []
with open('C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\LosAngelesCrimes.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        LACrimes.append(0)
  
#Boston      
BOCrimes = []
with open('C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\BostonCrimes.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        BOCrimes.append(0)