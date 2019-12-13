# -*- coding: utf-8 -*-
"""
Created on Sun Nov 9 19:03:22 2019

@author: Alex Marshall
Project Work with Data Mapping
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

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

'''
#keywords
Larceny
Burglary
Robbery
Assault
Drug
'''

#New York
def getNYCrimesByCode(csvFileLoc, codes, crimeWord):
    crimes = []
    csvLoc = baseDirectory + "NewYork" + crimeWord
    headerFlag = True
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
                for code in codes:
                    if rowPDCode == code: #row[8] is pdcode in NYCrimes.csv
                        crimes.append(row)
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
       
#getNYCrimesByCode(NYcsv, 379, 380, 397) 
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

#getSFCrimesByCode(SFcsv, 3474, 3401, 3071, 3023, 3012, 3044, 3054, 3014, 3011, 3072, 3472, 3024, 3063, 3022, 3414, 3073, 3444, 3052, 3084, 3464, 3081, 3013, 3412, 3051, 3053, 3471, 3473, 3043, 3034, 3021, 3421)
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
#getLACrimesByCode(LAcsv, 210, 220)       
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

#getBostonCrimesByCode(BOcsv, 301, 311, 351, 361, 371, 381)
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
#getChicagoCrimesByCodeAllCSVs("0312", "0313", "031A", "031B", "0320", "0325", "0326", "0330", "0331", "0334", "0337", "033A", "033B", "0340")
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

def makePieChartFromDescription(csvFileLoc, title, crime):
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
                codes.append(int(row[0]))
    print(sizes / total)
    return codes
#    sizes.sort()
#    plt.legend(labels, loc="best")
#    plt.axis('equal')
#    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
#    plt.title(title)
#    fig = plt.gcf()
#    fig.set_size_inches(18.5, 10.5)
#    fig.savefig(baseDirectory + title + '.png', dpi=100)
#    plt.show()      


csvLocSF = baseDirectory + "SanFranciscoCodesAndNo.csv"
#makePieChart(csvLocSF, "San Francisco Total Crime", 4000) 
#makePieChartFromDescription(csvLocSF, "abc", "Theft")
c = makePieChartFromDescription(csvLocSF, "abc", "Assault")     
getNYCrimesByCode(NYcsv, c, "Assault") 
    
csvLocLA = baseDirectory + "LosAngelesCodesAndNo.csv"
#makePieChart(csvLocLA, "Los Angeles Total Crime", 12000) 
#makePieChartFromDescription(csvLocLA, "Abc", "")


csvLocCO = baseDirectory + "ChicagoCodesAndNo.csv"
#makePieChart(csvLocCO, "Chicago Total Crime", 50000) 

csvLocBO = baseDirectory + "BostonCodesAndNo.csv"
#makePieChart(csvLocBO, "Boston Total Crime", 5000) 
#makePieChartFromDescription(csvLocBO, "Boston Total Crime", "Other") 

csvLocNY = baseDirectory + "NewYorkCodesAndNo.csv"
#makePieChart(csvLocNY, "New York Total Crime", 15000)   
#makePieChartFromDescription(csvLocNY, "New York Total Crime", "ROBBERY")  

def crimePerMonthBarChart(csvFileLoc, dateRow):
    crime = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    with open(csvFileLoc,'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        next(plots)
        for row in plots:
            try:
                date = row[dateRow]
                month = int(date[:2])
            except:
                print(row[dateRow])
            else:
                crime[month] += 1
    bars = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    y_pos = np.arange(len(bars))
    plt.bar(bars, height = crime[1:])
    plt.title(label = 'Robbery per month in New York')
    plt.xticks(y_pos, bars)
    plt.show()
    
#crimePerMonthBarChart(baseDirectory + "BostonCrimeCode_301_311_351_361_371_381.csv", 9)
#crimePerMonthBarChart(baseDirectory + "SanFranciscoCrimeCode_3474_3401_3071_3023_3012_3044_3054_3014_3011_3072_3472_3024_3063_3022_3414_3073_3444_3052_3084_3464_3081_3013_3412_3051_3053_3471_3473_3043_3034_3021_3421.csv", 1)
#crimePerMonthBarChart(baseDirectory + "ChicagoCrimeCode_0312_0313_031A_031B_0320_0325_0326_0330_0331_0334_0337_033A_033B_0340_From2001.csv", 3)        
#crimePerMonthBarChart(baseDirectory + "LosAngelesCrimeCode_210_220.csv", 1)
#crimePerMonthBarChart(baseDirectory + "NewYorkCrimeCode_379_380_397.csv", 1)