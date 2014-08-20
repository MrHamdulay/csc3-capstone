"""Show people who need to see advisors due to their dismal test marks
Haaroon Cassiem
11 May 2014"""

import math
def average(l):
    #function calculates average from file data in a list
    sum=0
    for i in range(len(l)):
        sum+=l[i][1]
    return sum/len(l)

def sd(l):
    #function calculates standard deviation from file data in a list
    a=average(l)
    variance=0
    for i in range(len(l)):
        variance+=(l[i][1]-a)**2
    return math.sqrt(variance/len(l))

def loadFile(f):
    #function loads file data into list
    loader=open(f,"r")
    data=[]
    for line in loader:
        splits=line.split(",")
        splits[1]=eval(splits[1])        
        data.append(splits)
        
    return data

if __name__=="__main__":
    f=input("Enter the marks filename:\n")
    l=loadFile(f)
    ave=average(l)
    s=sd(l)
    print("The average is: ","{0:.2f}".format(ave),"\nThe std deviation is: ","{0:.2f}".format(s),sep="")
    dunces=False
    for i in range(len(l)):
        if(l[i][1]<(ave-s)):
            if(not dunces):
                print("List of students who need to see an advisor:")
                dunces=True
            print(l[i][0])