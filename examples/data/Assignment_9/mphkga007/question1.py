"""" a Python program to analyse student marks read in from a file and determine which students need to see a student advisor.
kenneth mphele
13 may 2014"""

import math

def analyse(filename):
    #open file 
    f=open(filename, "r")
    #make a list of lines(readlines) then close the file
    lines=f.readlines()
    f.close
    mean=0
    #calculate the mean and put the marks in a list
    listmark=[]
    for i in range(len(lines)):
        lines[i]=lines[i][:-1].split(",")
        marks=int(lines[i][1])
        listmark.append(marks)
        mean+=marks
    mean=mean/len(lines)
    # calculate standard deviation
    standard=0
    string=listmark
    for mark in string:
        standard+=(int(mark)-mean)**2
    #print(standard,len(string))
    form="{m:.2f}"
    standard=math.sqrt(standard/len(string))
    std=form.format(m=standard)
    
    #calculate mark one standard below the mean
    below_the_mean=mean-standard
    
    #studendt who needs to see a student advisor
    result="{m:.2f}"
    print("The average is:",result.format(m=mean))
    print("The std deviation is:",std)
   
    students=[]
    for i in range(len(listmark)):
        if listmark[i]<below_the_mean:
            students.append(lines[i][0])
                            
                            
    if len(students)>0:
     print("List of students who need to see an advisor:")
     for i in students:
         print(i)
     
                
                
    
    
       
    

filename=input("Enter the marks filename:\n")

analyse(filename)
