#Azhar Abobbaker
#ABBAZH001
#14/05/2014

import math

def average(file):                      #average of numbers in file
    f=open(file, "r")
    lines=f.readlines()
    f.close()
    count=0
    mean=0
    for i in lines:
        count+=1
    for l in lines:
        if l[-1]=="\n":
            l=l[:-1]
        l=l.split(",")
        mean+=eval(l[1])
    return str(round(mean/count,2))

def standard_deviation(file):        #standard deviation of numbers from file
    f=open(file, "r")
    lines=f.readlines()
    f.close()
    count=0
    for i in lines:
        count+=1
    mean=eval(average(file))
    s=0
    for l in lines:
        if l[-1]=="\n":
            l=l[:-1]
        l=l.split(",")
        s+=(eval(l[1])-mean)**2
    sd=str(round(math.sqrt(s/count),2))
    return sd

def marks(file):                    #students need to see an advisor"""
    f=open(file, "r")
    lines=f.readlines()
    f.close()
    mean=eval(average(file))
    sd=eval(standard_deviation(file))
    names=[]
    for i in lines:
        if i[-1]=="\n":
            i=i[:-1]
        x=i.split(",")
        mark=eval(x[1])
        if mark < mean-sd:
            names.append(x[0])
    return names

def main():
    file=input("Enter the marks filename:\n")
    print("The average is:", "{0:0<5}".format(average(file)))
    print("The std deviation is:", "{0:0<4}".format(standard_deviation(file)))
    m=marks(file)
    if m:
        print("List of students who need to see an advisor:")
        for i in m:
            print(i)
    
main()    