#NOTE: I left a lot of my notes and debugging lines in the program so I could more
#easily remember what's going on when I look at it later on down the line

import math
import sys

class Loan(object):
    def __init__(self, principal, int_r, mo_pay):
        self.principal = principal
        self.int_r = int_r
        self.mo_pay = mo_pay

    def term(self):
        mr = self.int_r/12
        top = math.log(1 - mr * self.principal / self.mo_pay)
        bottom = math.log(1 + mr)
        n = -top / bottom
        return n
    
    def total_r_paid(self):
        n = self.term()
        total_paid = n * self.mo_pay
        r_paid = total_paid - self.principal
        return r_paid

def loan_info_collection():
    try:
        num_loans = input("How many loans are we talkin'?")
    except ValueError:
        print("\nDo you take me for a fool?!  Please only use integers!")
        
    loan_dict = {}
    i = 0
    while i < num_loans:
        i += 1
        #print i
        value_list = []
        try:
            p = input("""What is the principal on Loan %d?  Round to the nearest dollar.""" %(i)) 
            #print type(p)

        except ValueError:
            print("\nDo we really have to go through this again?  Integers!") #make this a variable value so it doesn't need to be repeated throughout the code
        value_list.append(p)
        try:
            r = input("""What is the interest rate on Loan %d?  Enter 6.8%% as 0.068""" %(i)) 
            #print type(r)
        except ValueError:
            print("\nOK, I understand.  This one was different.  Decimals now.")
        value_list.append(r)
        try:
            minm = input("""What is the minimum mo. payment on Loan %d?  Round to the nearest dollar.""" %(i)) 
            #print type(minm)
        except ValueError:
            print("\nDo we really have to go through this again?  Integers!")
        value_list.append(minm)
        loan_dict[i] = []
        loan_dict[i].append(value_list)
    try:
        maxpay = input("""last question, I promise.
        What is the maximum extra you can pay for all loans together?
        Round to the nearest dollar.""")
    except ValueError:
        print("\nDo we really have to go through this again?  Integers!")
    loan_dict[99] = maxpay
    print 'loan_dict: ', loan_dict                 
    return loan_dict
            
def scenarios():
    loans = loan_info_collection()
    #print 'loans: ', loans
    num_loans = len(loans) - 1
    #print 'num_loans: ', num_loans
    for i in range (1, num_loans + 1):
        #print 'i: ', i
        loan_stats = loans[i] ###this is [p, r, minm]
        #print 'loan_stats (begin): ', loan_stats
        maxpay = loans[99]
        term_list = []
        total_r_list = []
        
        for s in range(loan_stats[0][2], (loan_stats[0][2] + maxpay + 1)):
            loan = Loan(loan_stats[0][0], loan_stats[0][1], s)
            term_list.append(loan.term())
            total_r_list.append(loan.total_r_paid())
        loan_stats.append(term_list)
        loan_stats.append(total_r_list)
        loans[i] = loan_stats
        #print ('loan_stats (Loan %d): ' %(i)), loan_stats
    #print loans
    return loans 
   
def optimiser():
    loans = scenarios()
    num_loans = len(loans) - 1
##    print 'num_loans: ', num_loans
    for k, v in loans.iteritems(): #should i move this to scenarios()?
        if k == 99:
            continue
        if len(v) == 3:
            maxdollabills = []
            maxdollabills.append(len(v[2]) - 1)
            loans[k].append(maxdollabills)
        next_step = []
        curr_index = loans[k][3][0]
##        print curr_index
        next_step.append(loans[k][2][curr_index - 1] - loans[k][2][curr_index])
##        print next_step 
        if len(v) == 4:
            loans[k].append(next_step)
        loans[k][4] = next_step
    #print loans


    maxpay = loans[99]
    
    
    
    while True:
        total = 0
##        print '(inside while loop)', loans
##        print 'loans[1][3]: ', loans[1][3]
##        print 'loans[1][3][0]: ', loans[1][3][0]

        for k in loans:
            if k == 99:
                continue
##            print total
##            print 'k: ', k
##            print 'loans[k]: ', loans[k]
##            print 'loans[k][3]: ', loans[k][3]
##            print 'loans[k][3][0]: ', loans[k][3][0]
            total += loans[k][3][0]

        if total <= maxpay:
            results = {}
            for k in loans:
                if k == 99:
                    continue
                term = ['Term (months): ']
                addtl_pay = ["Addt'l Payment: "]
                total_r_paid = ['Total Interest Paid: ']
                final_index = loans[k][3][0]
                term.append(loans[k][1][final_index])
                addtl_pay.append(final_index)
                total_r_paid.append(loans[k][2][final_index])
                results_list = []
                results_list.append(term)    #can I append these 3 things at once?
                results_list.append(addtl_pay)
                results_list.append(total_r_paid)
                results[k] = results_list
            print results
            return results
        next_steps_list = []
        for k in loans:
            if k == 99:
                continue
            next_steps_list.append(loans[k][4][0])
        next_steps_list.sort()
        for k in loans:
            if k == 99:
                continue
            if loans[k][4][0] == next_steps_list[0]:
                loans[k][3][0] -= 1
                loans[k][4][0] = loans[k][2][loans[k][3][0] - 1] - loans[k][2][loans[k][3][0]]
        


                                                                    







            
            
    #Don't need to add the payments the first time, the index #s are the same as
    #the extra $ in the payment...so, just do len(loans[i][2]) - 1 for each entry in
    #dict to get the total payment.  That will be too high.  So, find the smallest
    #decrease moving down one in the index for each loan...will need to store the
    #current position for each loan.  Then do pull the value for current pos - 1
    
            
            
            
            
            
        
        
    
    
    
##    for k, v in loans.iteritems():
##   
##        total_r = [] #once this is created, add to dict
##        
##        str(Loan_%d %(d)) = Loan(principal = v[0], interest_rate = v[1], monthly_payment = v[2]) 
##           

      
        
####Do i even need a dictionary here?  Shouldn't the class be able to replace it?
####Seems like I could just create the list in loan_info_collection() and create a loan
####object for each as I go along?  Figure this out...


#def main():
#            
#        
#        
#    
#if __name__ == '__main__':
#    main()
#    





  








