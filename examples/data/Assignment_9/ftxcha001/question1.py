#Chantel Foot
#Assignment 9
#Question 1 


import math #import maths for neccesary calculations. 

def average (marks):
    #Function calculates the average of the given list 
    
    count=0 #start count at 0 
    
    for i in range(len(marks)):#need to convert every value in the list to integers
        count += int(marks[i]) # new count is the count before plus the new int of the value of in the list
        
    return (count/len(marks))  #want to return value to two decimal places

def std_dev(values):
    #Funtion calculates the SD of the values in the list     
    
    mean = average(values)           #need the average of the values in the list
    count = 0                        #Counter starting at 0. 
    
    for i in range(len(values)):
        count += (mean-int(values[i]))**2
        
    var=count/(len(values))      #Calculating variance which is SD squared. 
                 
    return (math.sqrt(var)) #return the value of the square root of variance which is equal to SD. 


def main():
    x=input("Enter the marks filename:\n")    # get an input from user i.e. the filename. 
    
    
    surnames = [] #empty strings. 
    percentage = []

    f=open(str(x), "r")                       #open the marks file. "r" means read file
    for line in f:                       #loop through each line in the file
    
        name=""
        mark=""
        for i in range (len(line)):   #loop through every character in the file
            
            if (line[i]).isalpha()==True: #checks if letter in alphabet
                name += line[i]
                
            if (line[i]).isdigit()==True: #checks if digit
                mark += line[i]
                
        surnames.append(name)         #add each name to the surname
        percentage.append(mark)       #add each mark to the % 
    f.close()                               #must close file. Saves contents. 
    
    
    drop_out= average(percentage)-std_dev(percentage)   #find mark in order to notify those students that need to see advisor.
    
    print("The average is: ", "{:.2f}".format(round(average(percentage), 2)), sep="")                                               #calcuating the average. formatting to 2 decimal places. 
    
    print("The std deviation is: ", "{:.2f}".format(round(std_dev(percentage), 2)), sep="")
    
    
    for i in percentage:
        if eval(i) < drop_out: #if less than drop out mark 
            print("List of students who need to see an advisor:")
            break #break loop. 
    
    for i in range(len(percentage)):  #checks mark with respect to the drop out mark 
        if eval(percentage[i]) < drop_out:
            print (surnames[i])
 
main()