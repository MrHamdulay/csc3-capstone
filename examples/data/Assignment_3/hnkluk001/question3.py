# Luke Henkeman
# HNKLUK001
# CSC1015F, Assignment 3, question 3
# 21 March 2014

def framed():
    msg = input("Enter the message:\n")
    rpt = eval(input("Enter the message repeat count:\n"))
    thick = eval(input("Enter the frame thickness:\n"))
    msg_length = len(msg)
    total_len = 2*thick + msg_length
    i=1
    if(thick>1):
        print("+",total_len*"-","+", sep='')
        j=1
        for j in range(1,thick,1):
            print(j*"|","+",(total_len-2*j)*"-","+",j*"|", sep='')
    elif (thick==0):print()    
    else:
        print("+",total_len*"-","+", sep='') 
    for i in range(i,rpt+1):
        print(thick*'|', msg, thick*'|')
    if(thick>1):
        j=1
        for j in range(thick-1,0,-1):
            print(j*"|","+",(total_len-2*j)*"-","+",j*"|", sep='')
        print("+",total_len*"-","+", sep='')        
    elif (thick == 0): print()    
    else:
        print("+",total_len*"-","+", sep='')
        
framed()