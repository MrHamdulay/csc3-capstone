#Sandisha Budhal
#Program analysing the marks of students
#15/05/2014

import math
def average_1(numb1):
    sum = 0.00                              
    for numb2 in numb1 :
        sum += numb2
    return (sum/ len(numb1))

def stand_dev(numb1,avg):
    sum1 = 0
    for numb2 in numb1:
        s_d = avg - numb2
        sum1 = sum1 + s_d**2    
    return (math.sqrt (( sum1 / len(numb1))))
                 
def file():
    filename= input("Enter the marks filename:\n") #asking the user to input the marks filename
    infile = open(filename,"r")
    diction={} #creating an empty dictionary
    for i in infile:
        learner = i.split(",") #splitting on the basis of ","
        diction[learner[0]] = [int(learner[1])]
    
    student_name = list(diction.keys())
    mrks = list(diction.values())
    Mrks=[] #creating an empty list
    for i in mrks:
        Mrks=Mrks+i
    avrg = average_1(Mrks)
    if (str(avrg))[3:] =="0":
        print("The average is: " + str(avrg)+"0")
    else:    
        print("The average is:",round(avrg,2))
        
    s_Dev = stand_dev(Mrks,avrg)
    if (str(s_Dev))[2:]=="0":
        print("The std deviation is: "+ str(s_Dev)+"0")
    else:    
        print("The std deviation is:",round(s_Dev,2))
    
    
    newlis=[] #creating a new list
    for mark in diction:
        if diction[mark][0] < int((avrg-s_Dev)):
            
            newlis.append(mark) #appending the new list with the mark
            
    if len(newlis)!=0:   #if the length of the new list is not equal to 0      
        print("List of students who need to see an advisor:\n",("\n").join(newlis),sep='')
        
    
file()   #calling the function
