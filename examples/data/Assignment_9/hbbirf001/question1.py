'''Data analyser
Irfan Habib
HBBIRF001
2014/05/11'''

import math # use math functions

filename = input('Enter the marks filename:\n')
f = open(filename,'r') #associate file on disk to variable
lines = f.readlines()   # read file contents to list
f.close         # close file to reduce risk of corrupting contents and/or memory allocation

def analyse():  
    '''calculate all the variables determined by the question'''
    sum = 0 # initialise counter
    for i in range(len(lines)): # loop to calculate sum
        s = lines[i].split(',') # separate the actual mark
        sum += int(s[1])
    average = round(sum/len(lines),2) # determine average
   
    sigma = 0   # initialise standard deviation
    for i in range(len(lines)): # start loop to calculate stand. dev.
        s = lines[i].split(',')
        sigma += (int(s[1]) - average)**2 
    sigma = round(math.sqrt(sigma/len(lines)),2) # stand. dev. calculated
   
    advisor = [] # initialise list to see advisor
    for i in range(len(lines)):
        s = lines[i].split(',') # separate the actual mark
        if int(s[1]) < (average-sigma):
            advisor.append(s[0])
            
    print('The average is:', "%0.2f" % average, sep=' ')
    print('The std deviation is:', "%0.2f" % sigma, sep = ' ')
    if len (advisor) != 0:
        print('List of students who need to see an advisor:')
        for i in range(len(advisor)):
            print(advisor[i])
    
analyse()

    
    
    
    
        
    