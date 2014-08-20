'''Program to analyse student marks
   Denzel Ncube
   10 May 2014'''

import math

filename = input("Enter the marks filename:\n")
f = open (filename,"r")
namelst = []
marklst = []
properlst = []
initiallst = [] 
initiallst = f.readlines()

#Getting a list without the \n
for i in range(len(initiallst)):
    initiallst[i] = initiallst[i].strip()
    properlst.append(initiallst[i])
    
#Seperating the names and marks into seperate lists
for j in range (len(properlst)):
    pos = properlst[j].index(',')
    name = properlst[j][:pos]
    mark = properlst[j][pos+1:]    
    marklst.append(mark)
    namelst.append(name)

#Function to get the average value of a list of floats     
def mean(lst):
    total = 0
    mean = 0
    for i in range(len(lst)):
        total += float(lst[i])
    mean = total / len(lst)
    return "%0.2f" % (mean)

#Function to get the standard deviation of a list of floats
def standarddev(lst):
    square = 0
    for i in range(len(lst)):
        square += (float(lst[i]) - float(mean(lst)))**2
    dev = math.sqrt(square/len(lst))
    return "%0.2f" % (dev)    

#Printing output
print("The average is:",mean(marklst))
print("The std deviation is:",standarddev(marklst))
#Function to print out the names of all students with marks less than one standard deviation from the mean
printlst = []
for i in range(len(properlst)):
    dev = float(standarddev(marklst))
    avg = float(mean(marklst))
    if float(marklst[i])+dev < avg:
        printlst.append(namelst[i])

#Printing out names only if there are any
if printlst != []:
    print("List of students who need to see an advisor:")    
for i in range(0,len(printlst)):
    print(printlst[i])
    
    

    
    

    



        
        
        
































f.close()
