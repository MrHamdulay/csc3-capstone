"""Assignment 9-Q1
Annika brundyn
11/05/2014"""

import math

#calculate average of list
def average (marks):
    counter=0
    #convert to integers
    for i in range(len(marks)):
        counter+= int(marks[i])
        
    return (counter/len(marks))

#calculate std deviation
def std_dev(values):
    mean=average(values)           
    counter=0                        
    for i in range(len(values)):
        counter+= (mean - int(values[i]))**2
        
    variance=counter/(len(values))      
                 
    return (math.sqrt(variance))        #variance = standard deviation^2


def main():
    #ask for filename
    filename =input("Enter the marks filename:\n")    
    
    surnames=[]
    percentage=[]
    
    #open file, iterate through each line
    f=open(str(filename), "r")                       
    for line in f:                 
        name=""
        mark=""
        for i in range (len(line)):   #iterate through each character
            
            if (line[i]).isalpha()==True:
                name=name+line[i]
            if (line[i]).isdigit()==True:
                mark=mark+line[i]
        surnames.append(name)         #add to surnames 
        percentage.append(mark)       #add to pecentages 
    f.close()                         
    
    #students who need to see advisor
    advisor= average(percentage)-std_dev(percentage) 
    
    #print out
    print("The average is: ", "{:.2f}".format(round(average(percentage), 2)), sep="")
    print("The std deviation is: ", "{:.2f}".format(round(std_dev(percentage), 2)), sep="")
    
    
    for i in percentage:
        if eval(i)<advisor:
            print("List of students who need to see an advisor:")
            break
    
    for i in range(len(percentage)):            
        if eval(percentage[i]) < advisor:
            print (surnames[i])

 
main()
