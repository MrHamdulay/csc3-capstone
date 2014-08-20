'''Sohail Tulsi 
TLSSOH001
14/05/2014
Programme to analyse student mark'''

import math

lis=[]
def file(filename):
#reads contents of file into 2d arrays
    f=open(filename,"r")
    content=f.readlines()
    for i in range(len(content)-1):
        x=content[i]
        x=x[:len(x)-1]
        content[i]=x
        lis.append(x.split(","))
    lis.append(content[len(content)-1].split(","))
    f.close()
    
def average():
    #calculates average mark
    add=0
    for i in range (len(lis)):
        add+=int(lis[i][1])
    average=(add/len(lis))
    
    return average

def stdDev(avr):
    #calculates the standard deviation of marks
    add=0
    for i in range (len(lis)):
        add+= (int(lis[i][1])-float(avr))**2
    
    stDev=(math.sqrt(add/len(lis)))
    return stDev    
    
def main():
    fileName=input("Enter the marks filename:\n")
    file(fileName)
    #for i in range (len(students)):
        #print(students[i][0], students[i][1])
    avr=float(average())
    stDev=float(stdDev(avr))
    print("The average is:","{0:0.2f}".format(avr))
    print("The std deviation is:","{0:0.2f}".format(stDev))
    
    dev1=avr-stDev
    lessDev=[]
    for i in range(len(lis)):
        if int(lis[i][1])<dev1:
            lessDev.append(lis[i][0])
    
    if len(lessDev)>0:
        print("List of students who need to see an advisor:")        
        for i in range(len(lessDev)):
            print(lessDev[i])        

main()