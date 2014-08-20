#GLNRUS002
#Assignment 9
#Question 1
#Analyse marks in file
import math

def getavg(col):#gets average of data sent to it
    avg=0
    count=0#used for dividng for total
    for i in col:
        tmp=i.split(",")#splits marks and names
        avg=avg+eval(tmp[1])#adds all marks to avg, initially
        count+=1#used for counting
    avg=avg/count#final avg calcculation
    return avg
        
def removetrail(l):#removes "\n" after every entry
    count=0
    for i in l:
        if count !=len(l)-1:
            l[count]=l[count][:-1]
        count+=1
    return l
        
def stddev(s,av):
    std=0#used to accumulate total
    count=0#used for counting
    
    for i in s:
        tmp=i.split(",")#used for analysing numbers after names
        std=std+((eval(tmp[1])-av)*(eval(tmp[1])-av))#firstly accumulating all vaues
        count+=1#used for indexing
    std=math.sqrt (std/count)
    return std

def flops(l,avg,std):
    count=0    
    floppers=[]
    for i in l:#runs through every entry for analysis
        tmp=i.split(",")
        if  eval(tmp[1])<(avg-std):#if outside std devuiation
            floppers.append(tmp[0])
        count+=1
    if floppers:#checks if there are flop stars
        print("List of students who need to see an advisor:")
        for i in floppers:
            print(i)
        
if __name__ == "__main__":
        fname=input("Enter the marks filename:\n")
        f=open (fname,"r")
        lines= f.readlines()
        f.close()    #done working with file
        lines=removetrail(lines)
        avg = getavg(lines) 
        print("The average is: {0:0.2f}".format(avg))
        std=stddev(lines,avg)
        print("The std deviation is: {0:0.2f}".format(std))
        flops(lines,avg,std)