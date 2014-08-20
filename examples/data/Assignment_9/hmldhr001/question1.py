
#Dhriven Hamlall

import math

def main():
    
    c=0 #counter
    StandardD=0    
    sum1=0

    NamesMarks=[]
 #=====================================================================================================   
    fileName=input("Enter the marks filename:\n")
    f=open(fileName,"r")
    for line in f:
        data=line.split(",")
        NamesMarks.append(data)
        c+=1
        sum1+=int(data[1])
        
    f.close()
    
    #================================================================================================ standard file work
   
   
   
    average=sum1/c
    for i in range(c):
        StandardD=StandardD+(int(NamesMarks[i][1])-average)**2 #by formula
    stdDev=math.sqrt((StandardD/c))
    #=================================================================================================
    
    print(("The average is: {0:"+str((len((str(average))[0:2])+1))+".2f}").format(average))
    print(("The std deviation is: {0:"+ str((len((str(stdDev))[0:2])+1))+".2f}").format(stdDev))
    
    t1=""
    TheList=[]
    
    for i in range(c):
        if int(NamesMarks[i][1])<(average-stdDev):
            TheList.append(NamesMarks[i][0])
            t1=NamesMarks[i][0]
    if t1!="":
        print("List of students who need to see an advisor:")
        for i in range(len(TheList)):
            print(TheList[i])
main() 