# List of Students who Need to See Advisor
# Sofia Palmer
# 12 May 2014

import math

#get rid of leading and ending quotes in each string
def strip_quotes (l):    
    for i in range (len (l)):
        if l[i] != "":
            if l[i][0] == '"':
                l[i] = l[i][1:]
            if l[i][-1] == '"':
                l[i] = l[i][:-1]
def main():
    
    filename = input("Enter the marks filename: \n")

    #open and load data from file
    f = open (filename, "r")   
    lines = f.readlines()
    f.close ()

    # get rid of trailing returns
    for i in range (len (lines)):
        lines[i] = lines[i][:-1]

    #get to grades
    N = 0
    average = 0
    for i in range (len(lines)):
        entries = lines[i].split(',')
        strip_quotes (entries)
        entries[1] = eval(entries[1])
        average += entries[1] 
        N = N+1
  
    average = average/N
 
    
    sd = 0
    for j in range(len(lines)):
        entries = lines[j].split (',')
        strip_quotes (entries)
        sd += (eval(entries[1]) - average)**2
    
    sd = math.sqrt(sd/N)
    
    print("The average is:", "{:.2f}".format(average))
    print("The std deviation is:", "{:.2f}".format(sd))
    
    for k in range(len(lines)):
        help = 1
        entries = lines[k].split (',')
        strip_quotes (entries) 
        if eval(entries[1]) < average - sd:
            help = 0 
        if (help == 0):
            print("List of students who need to see an advisor:")       
            print(entries[0])


main()
    
    
