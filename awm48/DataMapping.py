# -*- coding: utf-8 -*-
"""
Created on Sun Nov 9 19:03:22 2019

@author: Alex Marshall
Project Work with Data Mapping
"""
import csv
import numpy as np
import matplotlib.pyplot as plt

#CSVs
NYcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\NewYorkCrimes.csv'
SFcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\SanFranciscoCrimes.csv'
LAcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\LosAngelesCrimes.csv'
BOcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\BostonCrimes.csv'

#Key words to search by
ASSAULT = "assault"
BURGLARY = "burglary"
ROBBERY = "robbery"
LACERNY = "lacerny"
DRUG = "drug"

#New York

def getNYCrimesByCode(pdCode, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        crimes.append(next(plots))
        for row in plots:
            try:
                rowPDCode = int(row[8])
            except:
                1 + 1
            else:
                if rowPDCode == pdCode: #row[8] is pdcode in NYCrimes.csv
                    crimes.append(row)
        csvLoc = 'C:\\Users\\Regina\\Documents\\GitHub\\DSCI343Project\\awm48\\SortedData\\NewYorkCrimeCode' + str(pdCode) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)

getNYCrimesByCode(333, NYcsv)
'''
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

with open(SFcsv,'r') as csvfile:
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
'''
#Los Angeles     
LACrimes = []
with open(LAcsv,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        LACrimes.append(0)
  
#Boston      
BOCrimes = []
with open(BOcsv,'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        BOCrimes.append(0)
        
        
        
'''
Old code for parsing date 
def getNYCrimesByCode(pdCode, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        for row in plots:
            if pdCode == row[8]: #row[8] is pdcode in NYCrimes.csv
                date = row[1] #row[1] is date and time
                try:
                    month = int(date[:2].replace("/",""))
                    year = int(date[-4:])
                except:
                    print(date)
                else:
                    if year == 2014 | year == 2015:
                        NYCrimesMonth2014[month] = NYCrimesMonth2014[month] + 1
                    NYCrimesMonth2015[month] = NYCrimesMonth2015[month] + 1
'''