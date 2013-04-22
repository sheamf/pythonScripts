#SLPRecRuns.py

import csv
from decimal import *
import cmath
import time


def slpRunsDict():
    reader = csv.reader(open("C:\Users\miless\Desktop\SLP_Orders_Recurring_Runs_Scr.txt"))
    dict = {}
    testLimit = 0
    for row in reader:
        #if testLimit > 1000:
        #    break
        list = []
        #testLimit += 1
        if row[3] == 'C_RECURRING_ID':
            continue
        elif row[3] in dict:
            list = dict[row[3]]
            list.append(float(Decimal(row[2])))
            dict[row[3]] = list
        else:
            list.append(float(Decimal(row[2])))
            dict[row[3]] = list
    return dict
	
	
def valueRunsPairs():
    dict = slpRunsDict()
    vrPairs = []
    for v in dict.itervalues():
        onePair = []
        count = 0
        avgValue = 0
        for i in v:
            avgValue += i
        avgValue /= len(v)
        onePair.append(avgValue)
        count = len(v)
        onePair.append(count)
        vrPairs.append(onePair)
    return vrPairs
    
	
def slpRunCountList():
    dict = slpRunsDict()
    runCount = []
    for v in dict.itervalues():
        runCount.append(len(v))
    return runCount

def slpRunCountAgg():
    runCount = slpRunCountList()
    rcaDict = {}
    for i in runCount:
        if i in rcaDict:
            rcaDict[i] += 1
        else:
            rcaDict[i] = 1
    return rcaDict
    

    
print slpRunCountAgg()	
print valueRunsPairs()

	
	
	
		
	
	
	
	
	
	
	
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	


































    


    
