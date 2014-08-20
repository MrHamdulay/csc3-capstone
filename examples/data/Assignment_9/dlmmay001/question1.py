from math import *

def analyse():
    file = input('Enter the marks filename:\n')
    f = open(file,'r')
    lines = f.readline()
    MEA = []
    STD = []
    line = lines.split(',')
    MEA.append(eval(line[1])) 
    STD.append(line[1])
    k = 0
    names = []
    names.append(line[0])
    for lines in f:
        line = lines.split(',')
        MEA.append(eval(line[1]))
        STD.append(line[1])
        names.append(line[0])
        k+=1
   # print(STD)
    stdev = 0
    MEAN = sum(MEA)/(k+1)
    STDV = []
    for i in STD:
        
        std = (eval(i)-MEAN)**2
        STDV.append(std)
       # print(i)
    print('The average is: {0:0.2f}'.format(MEAN))
    #print(sum(STDV))
    stdevi = sqrt(sum(STDV)/(k+1))
    
    print('The std deviation is: {0:0.2f}'.format(stdevi))
    
  
    q = 0
    x = True
    for j in names:
        if eval(STD[q])<(MEAN-stdev):
            if x == True:
                print('List of students who need to see an advisor:')
                x = False
            print(j)
            
        q+=1
    
analyse()    