#was having trouble with this stalling out at a certain point in the txt file. 
#I never got a chance to figure out the cause, because the issue that necessitated
#creating this script as a check was fixed.

import csv
from collections import Counter
from time import clock

def bp_dict():
    time1 = clock()
    reader = csv.reader(open("C:\Users\miless\Desktop\dbo_ONP_XX_BPARTNER_PETS.txt"))
    bp_dict = {}
    for row in reader:
        dict_list = []
        row_list = []
        if row[6] == 'N':
            continue
        row_list.append(row[2])
        row_list.append(row[11])
        dict_list.append(row_list)
        if row[3] == 'C_BPARTNER_ID':
            continue
        elif row[3] in bp_dict:
            bp_dict[row[3]].append(row_list)
        else:
            bp_dict[row[3]] = dict_list
    time2 = clock()
    print 'bp_dict() ET: ' + str(time2-time1)
    return bp_dict
	
def pet_check():   # returns a list containing 'nd', 'nc', 'yd', 'yc' whether no or yes birthday, and dog or cat
    time1 = clock()
    bp_d = {}
    bp_d = bp_dict()
    for k, v in bp_d.iteritems():
        num_v = len(v)
        if num_v > 1:
            counter = 0
            types_list = []
            while counter < num_v:
                if v[counter][0] == '':
                    if v[counter][1][-1] == '0':
                        types_list.append('nd')
                    elif v[counter][1][-1] == '1':
                        types_list.append('nc')
                    else:
                        continue
                elif v[counter][0] != '':
                    if v[counter][1][-1] == '0':
                        types_list.append('yd')
                    elif v[counter][1][-1] == '1':
                        types_list.append('yc')
                counter += 1
            #print types_list    
            if 'nd' in types_list:
                if 'yd' in types_list:
                    print k + " 'nd' and 'yd'.  whoops..."
            if 'nc' in types_list:
                if 'yc' in types_list:
                    print k + " 'nc' and 'yc'.  whoops..."
    time2 = clock()
    print 'pet_check() ET: ' + str(time2-time1)

pet_check()








#i know this works at least, because i didn't filter out inactive pets, and a bunch were returned that would have qualified had they been active

       
##next step: build small test dataset to test all possibilities
##
##Need:
##bp1, nd
##bp1, yd (should catch this)
##bp2, nc
##bp2, yc (should catch this)
##bp3, nd
##bp3, yc (gtg)
##bp4, nc
##bp4, yd (gtg)
##bp5, yd 
##bp5, nc
##bp5, nd (should catch)
##bp6, yc 
##bp6, nd
##bp6, nc (should catch)
##(i think these last two might be unnecessary, since they're the first 2/3 of the previous two tests...)
##bp7, yc
##bp7, nd (gtg)
##bp8, yd
##bp8, nc (gtg)

##make the bps out of order to make sure it works like that.  should, b/c it's a dictionary, but...






    


                    
                
            
                











##last working stage:
##def pet_check():
##    bp_d = {}
##    bp_d = bp_dict()
##    print bp_d
##    for k, v in bp_d.iteritems():
##        num_v = len(v)
##        print num_v
##        if num_v > 1:
##            #print v[0]
##            if v[0][0] == '':
##                #print v[0][1]
##                if v[0][1][-1] == '0':
##                    print 'nd'
