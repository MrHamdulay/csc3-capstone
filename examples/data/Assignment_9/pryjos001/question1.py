"""Program to analyse student marks from a file
12 May 2014
Joseph Preyer"""

import math
filename = input("Enter the marks filename:\n")

def mark_analyse(filename):
    file = open(filename,"r") #open the file
    list1 = file.readlines() #read each line of the file into a list of strings
    file.close()
    list2=[]
    for i in range(len(list1)):#split each string within the list into the name and mark, and append to new list
        list2.append(list1[i].split(","))
    total=0
    for i in range (len(list2)): #get average
        total+= eval((list2[i][1][:2]))
    average=total/len(list2)
    print ("The average is:", "%0.2f"%average)
    std=0
    #get standard deviation
    for i in range (len(list2)):
        std+=(eval(list2[i][1][:2])-average)**2
    std=std/len(list2)
    std=math.sqrt(std)
    print ("The std deviation is:", "%0.2f"%std)
    
    #find which students have marks that are too low, and print their names
    x=""
    for i in range(len(list2)):
        if eval(list2[i][1][0:2])<(average-std):
            x +=(list2[i][0]+"\n")
    if len(x)>0:
        print("List of students who need to see an advisor:")
        print (x)
    
    
mark_analyse(filename)