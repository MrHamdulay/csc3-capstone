''' 
Program to analyse file of marks and determine who's 1sd below mean
frans van hoek
13 may 2014
'''

import math

def main():
    
    # get filename
    fname = input("Enter the marks filename:\n")
    
    # open file
    f = open(fname, "r")
    
    # create an empty list for marks and names (key)
    d = []
    
    for n in f.readlines():
        # split the name and the mark
        unit = n.split(",")
        # assign them to variables
        d.append(unit)
        
    f.close()
    
    # now find the mean
    total = 0
    c = 0
    for i in d:
        total += int(i[1])
        c += 1
    
    mean = total/c
    print ("The average is:", '%.2f' % mean)
    
    # now find standard deviation
    variance = 0
    for i in d:
        morsel = (int(i[1]) - mean)**2
        variance += morsel
        
    sd = math.sqrt(variance/c)
    print ("The std deviation is:", '%.2f' % sd)
    
    # define low threshold as one standard deviation under the mean
    lowest = mean - sd
    
    # now go through the dictionary and return those who have lower than that
    fail = []
    for i in d:
        if int(i[1]) < lowest:
            fail.append(i[0])
        
    if fail != []:
        print ("List of students who need to see an advisor:")
        for i in fail:
            print(i)
    
if __name__ == "__main__": main()
        
    
        
