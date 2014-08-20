#MAISHA IVHA
#12 MAY 2014
# APROGRAMME THAT ANALYZE STUDENT MARKS AND DETRMINE IF THE STUDENT NEEDS TO SEE A STUDENT ADVISOR

import math
def file_():
    filename=input("Enter the marks filename:\n")# getting the name of file with marks from the user
    infile=open(filename,"r")#opening the file for rading mode
    lines=infile.readlines()#reading the lines of the file
    
    
    '''creating a new list with mkarks to make calculation easier'''
    w=[]
    for line in lines:
        name,marks=line.split(",")#for each line split the name of student and marks
        w.append(marks)  #appending marks to the list

    '''calculating the sum of all the marks'''
    sum=0
    for i in range(len(w)):
        score=w[i]
        sum=sum+float(score)#converting the score in list w to an interger for calculation purposes     
                
    mean=sum/(len(w))#calculating the mean using score and length of list as number of scores
    
    '''calculating deviation'''
    deviation=0.00
    for j in range(len(w)):
        dev=mean-float(w[j]) #difference between mean and each score
        deviation=deviation+dev*dev 
    Sdev=math.sqrt(deviation/(len(w)))#calculating standard deviation with the maths function, square root imported
    ldev=mean-Sdev
    
    #rounded=round(Sdev,2)   #rounding the standard deviation to two decimal places
   
    print("The average is:","%.2f" %(mean))
    print("The std deviation is:","%.2f" %(Sdev))
    
    '''comparing score of marks with the name of students'''
    ad=[]
   # print(ad)
    for k in lines:
        name, marks_=k.split(",")# for every iterative in the marks that were splited form the list by a comma if the mark is gerater than the mean standard deviation, the corresponding name should be appended to the the ad list.
        if int(marks_)<ldev:
            #print(name)
            ad.append(name)
            #ad.appende(name)
    
        
    if ad!=[]: #if the list is not empty the programme should do print,
        print("List of students who need to see an advisor:")  
    for l in ad:
        print(l) #print every name in the list ad, these are the the students to see the advisor
    
file_()
        