# -*- coding: utf-8 -*-
"""
Created on Sun Nov 9 19:03:22 2019

@author: Alex Marshall
Project Work with Data Mapping
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
#CHANGE ME
baseDirectory = 'C:\\Users\\Regina\\Documents\\GitHub\\DSCI343Project\\awm48\\SortedData\\'

#CSVs
NYcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\NewYorkCrimes.csv'
SFcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\SanFranciscoCrimes.csv'
LAcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\LosAngelesCrimes.csv'
BOcsv = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\BostonCrimes.csv'
COcsv1 = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\ChicagoCrimes2001to2004.csv'
COcsv2 = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\ChicagoCrimes2005to2007.csv'
COcsv3 = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\ChicagoCrimes2008to2011.csv'
COcsv4 = 'C:\\Users\\Regina\\Documents\\Academics\\Fall 2019\\Data Analysis\\Project\\ChicagoCrimes2012to2017.csv'

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
        csvLoc = baseDirectory + "NewYorkCrimeCode" + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)

#getNYCrimesByCode(333, NYcsv)
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
        csvLoc = baseDirectory + "SanFranciscoCrimeCode" + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)


#getSFCrimesByCode(4134, SFcsv)
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
        csvLoc = baseDirectory + "LosAngelesCrimeCode" + str(code) + '.csv'
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
        csvLoc = baseDirectory + "BostonCrimeCode" + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)              
        
#getBostonCrimesByCode(3301, BOcsv)
#Chicago 
def getChicagoCrimesByCode(code, csvFileLoc):
    crimes = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        crimes.append(next(plots))
        for row in plots:
            r = row[5]
            if code == r:
                crimes.append(row)
        csvLoc = baseDirectory + "ChicagoCrimeCode" + str(code) + '.csv'
        with open(csvLoc, 'w', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(crimes)

#code for Chicago must be 4 characters long or it won't work           
getChicagoCrimesByCode("0486", COcsv4)