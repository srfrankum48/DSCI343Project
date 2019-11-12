# -*- coding: utf-8 -*-
"""
Created on Sun Nov 9 19:03:22 2019

@author: Alex Marshall
Project Work with Data Mapping
"""
import csv

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
COcsv = [COcsv1, COcsv2, COcsv3, COcsv4]

#New York
def getNYCrimesByCode(csvFileLoc, *codes):
    crimes = []
    csvLoc = baseDirectory + "NewYorkCrimeCode"
    headerFlag = True
    for code in codes:
        with open(csvFileLoc,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            if headerFlag:
                crimes.append(next(plots))
                headerFlag = False
            else:
                next(plots)
            for row in plots:
                try:
                    rowPDCode = int(row[8])
                except:
                    print(row[8])
                else:
                    if rowPDCode == code: #row[8] is pdcode in NYCrimes.csv
                        crimes.append(row)
        csvLoc += '_' + str(code)
    csvLoc += '.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)

#getNYCrimesByCode(NYcsv, 333, 511)
            
#San Francisco
def getSFCrimesByCode(csvFileLoc, *codes):
    crimes = []
    csvLoc = baseDirectory + "SanFranciscoCrimeCode"
    headerFlag = True
    for code in codes:
        with open(csvFileLoc,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            if headerFlag:
                crimes.append(next(plots))
                headerFlag = False
            else:
                next(plots)
            for row in plots:
                try:
                    rowPDCode = int(row[13])
                except:
                    print(row[13])
                else:
                    if rowPDCode == code: #row[13] is category code in SFCrimes.csv
                        crimes.append(row)
        csvLoc += '_' + str(code)
    csvLoc += '.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)

#getSFCrimesByCode(SFcsv, 4134, 28160)

#Los Angeles     
def getLACrimesByCode(csvFileLoc, *codes):
    crimes = []
    csvLoc = baseDirectory + "LosAngelesCrimeCode"
    headerFlag = True
    for code in codes:
        with open(csvFileLoc,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            if headerFlag:
                crimes.append(next(plots))
                headerFlag = False
            else:
                next(plots)
            for row in plots:
                try:
                    rowCode = int(row[7])
                except:
                    print(row[7])
                else:
                    if rowCode == code:
                        crimes.append(row)
        csvLoc += '_' + str(code)
    csvLoc += '.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)
 
#getLACrimesByCode(LAcsv, 510, 626)
        
#Boston      
def getBostonCrimesByCode(csvFileLoc, *codes):
    crimes = []
    csvLoc = baseDirectory + "BostonCrimeCode"
    headerFlag = True
    for code in codes:
        with open(csvFileLoc,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            if headerFlag:
                crimes.append(next(plots))
                headerFlag = False
            else:
                next(plots)
            for row in plots:
                try:
                    rowCode = int(row[1])
                except:
                    print(row[1])
                else:
                    if rowCode == code:
                        crimes.append(row)
        csvLoc += '_' + str(code)
    csvLoc += '.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)              
        
#getBostonCrimesByCode(BOcsv, 612, 613)
        
#Chicago 
def getChicagoCrimesByCode(csvFileLoc, *codes):
    crimes = []
    csvLoc = baseDirectory + "ChicagoCrimeCode"
    headerFlag = True
    for code in codes:
        with open(csvFileLoc,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            if headerFlag:
                crimes.append(next(plots))
                headerFlag = False
            else:
                next(plots)
            for row in plots:
                try:
                    r = row[5]
                except:
                    print(row[5])
                else:
                    if r == code:
                        crimes.append(row)
        csvLoc += '_' + str(code)
    csvLoc += '.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)
        
def getChicagoCrimesByCodeAllCSVs(*codes):
    crimes = []
    csvLoc = baseDirectory + "ChicagoCrimeCode"
    headerFlag = True
    for code in codes:
        for c in COcsv:
            with open(c,'r') as csvfile:
                plots = csv.reader(csvfile, delimiter=',')
                if headerFlag:
                    crimes.append(next(plots))
                    headerFlag = False
                else:
                    next(plots)
                for row in plots:
                    try:
                        r = row[5]
                    except:
                        print(row[5])
                    else:
                        if r == code:
                            crimes.append(row)
        csvLoc += '_' + str(code)
    csvLoc += '_From2001.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)

#code for Chicago must be 4 characters long or it won't work           
#getChicagoCrimesByCode(COcsv4, "0486", "0820")
#getChicagoCrimesByCodeAllCSVs("0486")