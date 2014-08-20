#Assignment 9 Question 1
#Dean Bunce
#Program to check whether students need to see an advisor
#11 May 2014

import math

def main():
    
    #Get input
    filename= input("Enter the marks filename: \n")
    
    open_file=open(filename, "r")
    
    open_file.readlines
    
    #Set Variables to 0/empty
    stddev_total=0
    total=0
    n=0
    name_order=[]
    gradebook={}
    
    
    for line in open_file:
        
        #Split the names and marks and add them to a list, then a dictionary
        names, marks=line.split(",")
        
        name_order.append(names)
        gradebook[names]=marks
        
        
        total+=int(marks)
        n+=1
    
    #Calculate the mean
    mean=total/n
    
    #Calculate the total of standard deviation
    for names in gradebook:
        
        stddev_total+=(mean-int(gradebook[names]))**2
        
    #Calculate actual standard deviation
    stddev=math.sqrt((stddev_total)/n)
    
    
    
    print("The average is:", "{0:.2f}".format(mean))
    
    print("The std deviation is: " "{0:.2f}".format(stddev))
    
    #Print out the heading for the list of names-if it is necessary
    count=0
    for names in name_order:
        if int(gradebook[names])<(mean-stddev) and count==0:
            count+=1
            print("List of students who need to see an advisor:")
    
    
    #Print out the names from the dictionary in the order that they were inputted
    for names in name_order:
        if int(gradebook[names])<(mean-stddev):
            print(names)
            
            
    open_file.close()
    
       
main()        
        