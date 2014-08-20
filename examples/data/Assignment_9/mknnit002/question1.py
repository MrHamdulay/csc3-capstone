#program to determine which students need to see an advisor.
#mknnit002
#ass 9 question 1

import math

def average (marks):
    """"calculates average of a list"""
    total=0
    for i in range(len(marks)):#converts all values to integers
        total= total+int(marks[i])
        
    return (total/len(marks))  #find average

def stand_dev(values):
    """calculate standard deviation of values"""
    
    mean=average(values)           #get the average of the values
    total=0                        #set total variable equal to 0
    for i in range(len(values)):
        total=total+(mean - int(values[i]))**2  
        
    variance=total/(len(values))      # finding variance
                 
    return (math.sqrt(variance))  #finding standard deviation


def main():
    x=input("Enter the marks filename:\n")    # get input from user
                        
    
    surnames=[]
    percentage=[]

    f=open(str(x), "r")                       #open the file
    for line in f:                 # loop through the file
    
        name=""
        mark=""
        for i in range (len(line)):   #iterate through the file
            
            if (line[i]).isalpha()==True:
                name=name+line[i]
            if (line[i]).isdigit()==True:
                mark=mark+line[i]
        surnames.append(name)         #append name to surnames 
        percentage.append(mark)       #append mark to pecentages 
    f.close()                               #close file
    
    
    dropout= average(percentage)-stand_dev(percentage)   #find mark for which people need to see advisor
    
    print("The average is: ", "{:.2f}".format(round(average(percentage), 2)), sep="")
    print("The std deviation is: ", "{:.2f}".format(round(stand_dev(percentage), 2)), sep="")
    
    
    for i in percentage:
        if eval(i)<dropout:
            print("List of students who need to see an advisor:")
            break
    
    for i in range(len(percentage)):  #checks mark against drop out mark 
        if eval(percentage[i]) < dropout:
            print (surnames[i])
 
        
  

main()