#csvReader.py

import csv
from decimal import *
import cmath
import time 

def orderSubTotal():
    #import csv
    reader = csv.reader(open("C:\Users\miless\Desktop\(trimmed)_ONP_C_ORDER_10012012_Scr.txt"))
    orderSubTotal = {}
    
    for row in reader:
##        print row[0]
        if row[14] == 'GRANDTOTAL':
##            print row[0]
            continue
        orderSubTotal[row[6]] = row[14]
    return orderSubTotal

def orderSubTotalSum():
    #from decimal import Decimal 
    orderSubTotalDict = orderSubTotal()
    orderSubTotalSum = 0
    for order in orderSubTotalDict:
        orderSubTotalSum +=  float(Decimal(orderSubTotalDict[order]))
    return orderSubTotalSum

def orderCount():
    orderCount = len(orderSubTotal())
    return orderCount

def orderSubTotalList():
    orderSubTotalDict = orderSubTotal()
    orderSubTotalList = []
    for order in orderSubTotalDict:
        orderSubTotalList.append(float(Decimal(orderSubTotalDict[order])))
    orderSubTotalList.sort()
    return orderSubTotalList

def orderSubTotalMean():
    orderSubTotalMean = orderSubTotalSum() / orderCount()
    return orderSubTotalMean

def orderSubTotalMedian():
    list = orderSubTotalList()
    if len(list)%2 == 1:
        #Used for testing, returns result of int division and list length
        #return 1, len(list), list[int((len(list)/2.0) - 0.5)]
    #return 0, len(list), (list[int(len(list)/2.0)] + \
           #list[int((len(list)/2.0) - 1)]) / 2
        return list[int((len(list)/2.0) - 0.5)]
    return (list[int(len(list)/2.0)] + \
           list[int((len(list)/2.0) - 1)]) / 2

def orderSubTotalVariance():
    ###NEED A BETTER VARIANCE ALGORITHM.  Learn about a few and pick one...
    mean = orderSubTotalMean()
    devMeanList = []
    list = orderSubTotalList()
    listSquared = []
    for amt in list:
        devMeanList.append(amt - mean)
    for dev in devMeanList:
        listSquared.append(dev**2)
    sumListSquared = 0
    for p in listSquared:
        sumListSquared += p  
    #return sumListSquared, len(listSquared), sumListSquared / len(listSquared)
    return sumListSquared / len(listSquared)

def orderSubTotalStdDev():
    #stdDev = cmath.sqrt(orderSubTotalVariance())
    stdDev = orderSubTotalVariance() ** 0.5
    return stdDev

	
#this is it's own fucntion (rather than __main__) so the others can be called seperately when running the program if needed	
def orderSubTotalDescStats():
    print 'Number of Orders:', orderCount()
    print 'Order Sub Total Measures:'
    print '    +Total Value:', orderSubTotalSum()
    print '    +Arithmetic Mean:', orderSubTotalMean()
    print '    +Median:', orderSubTotalMedian()
    print '    +Variance:', orderSubTotalVariance()
    print '    +Standard Deviation:', orderSubTotalStdDev()
    

    
                             
                        
##startTime = time.clock()
##print orderSubTotalDescStats()
##print time.clock() - startTime, 'seconds'

#Timed Runs 
#1: 195.246s
#2: 




##def orderSubTotalDesc():
    

##Questions:
##    1. is it best to turn the dictionary values into numbers when the
##       dictionary is created, or should I do it separately each time I
##       need to perform operations on the values?  Is there any reason
##       to keep them as strings?



































    


    
