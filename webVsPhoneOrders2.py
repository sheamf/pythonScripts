#webVsPhoneOrders.py

#orderSubTotalHist.py
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import csv
from decimal import *
import cmath

def phoWebOrdST(PhoWebSLP):
    #import csv
    reader = csv.reader(open("C:\Users\miless\Desktop\ONPSStats\dboOrdersScr.txt"))
    orderST = []
    for row in reader:
        if row[13][:3] == PhoWebSLP:
            orderST.append(float(Decimal(row[3])))
        else:
            continue
    orderST.sort()
    return orderST

def orderSTSum(PhoWebSLP):
    #from decimal import Decimal 
    orderSTList = phoWebOrdST(PhoWebSLP)
    orderSTSum = 0
    for subTotal in orderSTList:
        orderSTSum +=  subTotal
    return orderSTSum

def orderCount(PhoWebSLP):
    orderCount = len(phoWebOrdST(PhoWebSLP))
    return orderCount

def orderSubTotalMean(PhoWebSLP):
    orderSubTotalMean = orderSTSum(PhoWebSLP) / orderCount(PhoWebSLP)
    return orderSubTotalMean

def orderSubTotalMedian(PhoWebSLP):
    list = phoWebOrdST(PhoWebSLP)
    if len(list)%2 == 1:
    #Used for testing, returns result of int division and list length
        #return 1, len(list), list[int((len(list)/2.0) - 0.5)]
    #return 0, len(list), (list[int(len(list)/2.0)] + \
           #list[int((len(list)/2.0) - 1)]) / 2
        return list[int((len(list)/2.0) - 0.5)]
    return (list[int(len(list)/2.0)] + \
           list[int((len(list)/2.0) - 1)]) / 2

def orderSubTotalVariance(PhoWebSLP):
    ###NEED A BETTER VARIANCE FORMULA.  Learn about a few and pick one...
    mean = orderSubTotalMean(PhoWebSLP)
    devMeanList = []
    list = phoWebOrdST(PhoWebSLP)
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

def orderSubTotalStdDev(PhoWebSLP):
    #stdDev = cmath.sqrt(orderSubTotalVariance())
    stdDev = orderSubTotalVariance(PhoWebSLP) ** 0.5
    return stdDev

def orderSubTotalDescStats(PhoWebSLP):
    print 'Number of Orders:', orderCount(PhoWebSLP)
    print 'Order Sub Total Measures:'
    print '    +Total Value:', orderSTSum(PhoWebSLP)
    print '    +Arithmetic Mean:', orderSubTotalMean(PhoWebSLP)
    print '    +Median:', orderSubTotalMedian(PhoWebSLP)
    print '    +Variance:', orderSubTotalVariance(PhoWebSLP)
    print '    +Standard Deviation:', orderSubTotalStdDev(PhoWebSLP)
    
print "Phone, Web, or SLP?  Enter 'Pho', 'Web', or 'SLP'."
PhoWebSLP = input()
orderSubTotalDescStats(PhoWebSLP)

plt.hist(phoWebOrdST(PhoWebSLP),bins = 250,range = (0, 250), normed = False, weights=None, \
     cumulative=False, bottom=None, histtype='bar', align='mid', \
     orientation='vertical', rwidth=None, log=False, \
     color=None, label=None)

plt.show()
















