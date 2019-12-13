# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 16:37:27 2019

@author: Regina
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
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

def createCSVOfCrimesByCode(crimeCodeRow, codes, crimeWord, city, *csvFileLocs):
    crimes = []
    csvLoc = baseDirectory + city + crimeWord
    headerFlag = True
    for csvFileLoc in csvFileLocs:
        with open(csvFileLoc,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            if headerFlag:
                crimes.append(next(plots))
                headerFlag = False
            else:
                next(plots)
            for row in plots:
                try:
                    rowPDCode = int(row[crimeCodeRow])
                    rowPDCodeString = row[crimeCodeRow]
                except:
                    1 + 1
                    #print(row[crimeCodeRow])
                else:
                    for code in codes:
                        try:
                            if rowPDCode == code: #row[8] is pdcode in NYCrimes.csv
                                crimes.append(row)
                        except:
                            if rowPDCodeString == code:
                                crimes.append(row)                     
    csvLoc += '.csv'
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(crimes)
        
def getCrimeCodeByCrime(csvFileLoc, crime):
    sizes = 0
    codes = []
    total = 0
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            total += int(row[2])
            if crime.lower() in row[1].lower() :
                sizes += int(row[2])
                try:
                    codes.append(int(row[0]))
                except:
                    codes.append(row[0])
    print(sizes / total)
    return codes    

keyword = "Drug"
createCSVOfCrimesByCode(8, getCrimeCodeByCrime(baseDirectory + "NewYorkCodesAndNo.csv", keyword), keyword, "NewYork", NYcsv)
createCSVOfCrimesByCode(13, getCrimeCodeByCrime(baseDirectory + "SanFranciscoCodesAndNo.csv", keyword), keyword, "SanFrancisco", SFcsv)
createCSVOfCrimesByCode(7, getCrimeCodeByCrime(baseDirectory + "LosAngelesCodesAndNo.csv", keyword), keyword, "LosAngeles", LAcsv)
createCSVOfCrimesByCode(1, getCrimeCodeByCrime(baseDirectory + "BostonCodesAndNo.csv", keyword), keyword, "Boston", BOcsv)
createCSVOfCrimesByCode(5, getCrimeCodeByCrime(baseDirectory + "ChicagoCodesAndNo.csv", keyword), keyword, "Chicago", COcsv1, COcsv2, COcsv3, COcsv4)
