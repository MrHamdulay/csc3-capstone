#Amitha Doodnath - DDNAMI001
#14/05/2014
#Programme to analyse student marks according to 1 standard deviation from the mean

import math

students=[]
def file(fileName):
#reads contents of file into 2d arrays
    f=open(fileName,"r")
    content=f.readlines()
    for i in range(len(content)-1):
        x=content[i]
        x=x[:len(x)-1]
        content[i]=x
        students.append(x.split(","))
    students.append(content[len(content)-1].split(","))
    f.close()
    
def average():
    #calculates average mark
    sum=0
    for i in range (len(students)):
        sum+=int(students[i][1])
    average=(sum/len(students))
    
    return average

def stdDev(avr):
    #calculates the standard deviation of marks
    sum=0
    for i in range (len(students)):
        sum+= (int(students[i][1])-float(avr))**2
    
    stDev=(math.sqrt(sum/len(students)))
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
    for i in range(len(students)):
        if int(students[i][1])<dev1:
            lessDev.append(students[i][0])
    
    if len(lessDev)>0:
        print("List of students who need to see an advisor:")        
        for i in range(len(lessDev)):
            print(lessDev[i])        

main()