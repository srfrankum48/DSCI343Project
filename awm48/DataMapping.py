# -*- coding: utf-8 -*-
"""
Created on Sun Nov 9 19:03:22 2019

@author: Alex Marshall
Project Work with Data Mapping
"""
import csv
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

def getAllOffenseCodesNY(csvFileLoc):
    codes = []
    codes.append(["Code", "Code Description", "Number of Occurences"])
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            try:
                rowCode = int(row[8])
                rowCodeDesc = row[9]
            except:
                print(row[8])
                print(row[9])
            else:
                #check if the code and desc exist in codes then add one to their total number
                if rowCodeDesc == "":
                    print("No row code description: ", rowCode)
                elif any(((rowCode in sublist) & (rowCodeDesc in sublist)) for sublist in codes):
                    for i in range(len(codes)):
                        if (codes[i][0] == rowCode) & (codes[i][1] == rowCodeDesc):
                            codes[i][2] += 1
                            break
                #Else (code and desc dont exist) add code and description to codes, set total number to 1
                else:
                    codes.append([rowCode, rowCodeDesc, 1])
    csvLoc = baseDirectory + "NewYorkCodesAndNo.csv"
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(codes)
        
#getNYCrimesByCode(NYcsv, 333, 511)
#getAllOffenseCodesNY(NYcsv)          
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

def getAllOffenseCodesSF(csvFileLoc):
    codes = []
    codes.append(["Code", "Code Description", "Number of Occurences"])
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            try:
                rowCode = int(row[13])
                rowCodeDesc = row[14]
            except:
                print(row[13])
                print(row[14])
            else:
                #check if the code and desc exist in codes then add one to their total number
                if rowCodeDesc == "":
                    print("No row code description: ", rowCode)
                elif any(((rowCode in sublist) & (rowCodeDesc in sublist)) for sublist in codes):
                    for i in range(len(codes)):
                        if (codes[i][0] == rowCode) & (codes[i][1] == rowCodeDesc):
                            codes[i][2] += 1
                            break
                #Else (code and desc dont exist) add code and description to codes, set total number to 1
                else:
                    codes.append([rowCode, rowCodeDesc, 1])
    csvLoc = baseDirectory + "SanFranciscoCodesAndNo.csv"
    codes[0].sort()
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(codes)

#getSFCrimesByCode(SFcsv, 4134, 28160)
#getAllOffenseCodesSF(SFcsv)
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

def addToRowCode(rowCode, rowCodeDesc, codes):
    for sublist in codes:
        if sublist[0] == rowCode & (sublist[1] == rowCodeDesc):
            sublist[2] += 1
            return codes
    return codes

def getAllOffenseCodesLA(csvFileLoc):
    codes = []
    codes.append(["Code", "Code Description", "Number of Occurences"])
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            try:
                rowCode = int(row[7])
                rowCodeDesc = row[8]
            except:
                print(row[7])
                print(row[8])
            else:
                #check if the code and desc exist in codes then add one to their total number
                if rowCodeDesc == "":
                    print("No row code description: ", rowCode)
                elif any(((rowCode in sublist) & (rowCodeDesc in sublist)) for sublist in codes):
                    for i in range(len(codes)):
                        if (codes[i][0] == rowCode) & (codes[i][1] == rowCodeDesc):
                            codes[i][2] += 1
                            break
                #Else (code and desc dont exist) add code and description to codes, set total number to 1
                else:
                    codes.append([rowCode, rowCodeDesc, 1])
    csvLoc = baseDirectory + "LosAngelesCodesAndNo.csv"
    codes[0].sort()
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(codes)
            
#getAllOffenseCodesLA(LAcsv)  
        
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

def getAllOffenseCodesBO(csvFileLoc):
    codes = []
    codes.append(["Code", "Code Description", "Number of Occurences"])
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            try:
                rowCode = int(row[1])
                rowCodeDesc = row[2]
            except:
                print(row[1])
                print(row[2])
            else:
                #check if the code and desc exist in codes then add one to their total number
                if rowCodeDesc == "":
                    print("No row code description: ", rowCode)
                elif any(((rowCode in sublist) & (rowCodeDesc in sublist)) for sublist in codes):
                    for i in range(len(codes)):
                        if (codes[i][0] == rowCode) & (codes[i][1] == rowCodeDesc):
                            codes[i][2] += 1
                            break
                #Else (code and desc dont exist) add code and description to codes, set total number to 1
                else:
                    codes.append([rowCode, rowCodeDesc, 1])
    csvLoc = baseDirectory + "BostonCodesAndNo.csv"
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(codes)        

#getBostonCrimesByCode(BOcsv, 612, 613)
#getAllOffenseCodesBO(BOcsv)        
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


def getAllOffenseCodesCO():
    codes = []
    codes.append(["Code", "Code Description", "Number of Occurences"])
    for csvs in COcsv:
        with open(csvs,'r') as csvfile:
            plots = csv.reader(csvfile, delimiter=',')
            next(plots)
            for row in plots:
                try:
                    rowCode = row[5]
                    rowCodeDesc = row[6]
                except:
                    print(row[5])
                    print(row[6])
                else:
                    #check if the code and desc exist in codes then add one to their total number
                    if rowCodeDesc == "":
                        print("No row code description: ", rowCode)
                    elif any(((rowCode in sublist) & (rowCodeDesc in sublist)) for sublist in codes):
                        for i in range(len(codes)):
                            if (codes[i][0] == rowCode) & (codes[i][1] == rowCodeDesc):
                                codes[i][2] += 1
                                break
                    #Else (code and desc dont exist) add code and description to codes, set total number to 1
                    else:
                        codes.append([rowCode, rowCodeDesc, 1])
    csvLoc = baseDirectory + "ChicagoCodesAndNo.csv"
    with open(csvLoc, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(codes)
#code for Chicago must be 4 characters long or it won't work           
#getChicagoCrimesByCode(COcsv4, "0486", "0820")
#getChicagoCrimesByCodeAllCSVs("0486")
#getAllOffenseCodesCO()
        
#Pie Charts
        
def makePieChart(csvFileLoc, title, crimeLimit):
    sizes = []
    labels = []
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            if int(row[2]) > crimeLimit:
                sizes.append(int(row[2]))
                labels.append(row[1])
    sizes.sort()
    plt.legend(labels, loc="best")
    plt.axis('equal')
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig(baseDirectory + title + '.png', dpi=100)
    plt.show()     

#csvLocSF = baseDirectory + "SanFranciscoCodesAndNo.csv"
#makePieChart(csvLocSF, "San Francisco Total Crime", 4000) 

#csvLocSF = baseDirectory + "LosAngelesCodesAndNo.csv"
#makePieChart(csvLocSF, "Los Angeles Total Crime", 12000) 

#csvLocSF = baseDirectory + "ChicagoCodesAndNo.csv"
#makePieChart(csvLocSF, "Chicago Total Crime", 50000) 

#csvLocSF = baseDirectory + "BostonCodesAndNo.csv"
#makePieChart(csvLocSF, "Boston Total Crime", 5000) 

#csvLocSF = baseDirectory + "NewYorkCodesAndNo.csv"
#makePieChart(csvLocSF, "New York Total Crime", 15000)            