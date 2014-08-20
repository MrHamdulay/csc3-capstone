#CSC1015F 
#ASSIGNMENT 6
#QUESTION 4
#WHTBAS001
#23/04/2014

import collections

def mark_catagory(x):
    for i in range(len(x)):
        x[i] = eval(x[i]) #converts string into numbers
        if x[i] >= 75:
            x[i] = '1' #puts mark into first category if cond met
        elif x[i] >= 70:
            x[i] = '2+' #puts mark into 2+ category if cond met
        elif x[i] >= 60:
            x[i] = '2-' #puts mark into 2- category if cond met
        elif x[i] >= 50:
            x[i] = '3' #puts mark into third category if cond met
        else:
            x[i] = 'F' #puts mark into F category if no cond met
        
        
instring = input("Enter a space-separated list of marks:\n")
marklist = instring.split() #splits input string marks into list
    
mark_catagory(marklist)

def final(x):
    c = collections.Counter() #create new counter subdictionary
    for i in x:
        c[i]+=1 #word in list added to dictionary as key then +1 to value
    y = ['1', '2+','2-','3','F'] #Mark brackets in order!
    for j in y:
        r = "{0:<2}".format(j) + "|" + "X"*(c[j]) #generates string of output
        print(r)

final(marklist)