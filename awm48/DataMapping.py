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
def getNYCrimesByCode(code, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        crimes.append(next(plots))
        for row in plots:
            try:
                rowPDCode = int(row[8])
            except:
                print(row[8])
            else:
                if rowPDCode == code: #row[8] is pdcode in NYCrimes.csv
                    crimes.append(row)
        csvLoc = 'C:\\Users\\Regina\\Documents\\GitHub\\DSCI343Project\\awm48\\SortedData\\NewYorkCrimeCode' + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)

#getNYCrimesByCode(333, NYcsv)
#data = NYCrimesMonth2014[1:13]
#print(data)
#bars = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec') 
#y_pos = np.arange(len(bars))      
#plt.bar(bars, data)
#plt.title(label = 'Crimes per month in LA')
#plt.xticks(y_pos, bars)
#plt.show()

#San Francisco
def getSFCrimesByCode(code, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        crimes.append(next(plots))
        for row in plots:
            try:
                rowPDCode = int(row[13])
            except:
                print(row[13])
            else:
                if rowPDCode == code: #row[13] is category code in SFCrimes.csv
                    crimes.append(row)
        csvLoc = 'C:\\Users\\Regina\\Documents\\GitHub\\DSCI343Project\\awm48\\SortedData\\SanFranciscoCrimeCode' + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)

'''
getSFCrimesByCode(4134, SFcsv)
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
def getLACrimesByCode(code, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        crimes.append(next(plots))
        for row in plots:
            try:
                rowCode = int(row[7])
            except:
                print(row[7])
            else:
                if rowCode == code:
                    crimes.append(row)
        csvLoc = 'C:\\Users\\Regina\\Documents\\GitHub\\DSCI343Project\\awm48\\SortedData\\LosAngelesCrimeCode' + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)
 
#getLACrimesByCode(510, LAcsv)
#Boston      
def getBostonCrimesByCode(code, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        crimes.append(next(plots))
        for row in plots:
            try:
                rowCode = int(row[1])
            except:
                print(row[1])
            else:
                if rowCode == code:
                    crimes.append(row)
        csvLoc = 'C:\\Users\\Regina\\Documents\\GitHub\\DSCI343Project\\awm48\\SortedData\\BostonCrimeCode' + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)              
        
getBostonCrimesByCode(3301, BOcsv)