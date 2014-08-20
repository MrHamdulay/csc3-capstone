"""Assignment9 Question1 
determine which students need to see a student advisor
Shaheen Karodia
KRDSHA003
2014-05-10"""

import math

def average (marks):
    """"calculates average of a list"""
    total=0
    for i in range(len(marks)):#convert all values in the list to integers
        total= total+int(marks[i])
        
    return (total/len(marks))  #format to two decimal places

def stand_dev(values):
    """calculate standard deviation of values"""
    
    mean=average(values)           #get the average of the values
    total=0                        #initialise total variable
    for i in range(len(values)):
        total=total+(mean - int(values[i]))**2
        
    variance=total/(len(values))      #variance is the squared value of standard deviation
                 
    return (math.sqrt(variance))


def main():
    x=input("Enter the marks filename:\n")    # get input from user
                          #open the file
    
    surnames=[]
    percentage=[]

    f=open(str(x), "r")                       #open the file
    for line in f:                 #go through each line of the file
    
        name=""
        mark=""
        for i in range (len(line)):   #iterate through each character of the file
            
            if (line[i]).isalpha()==True:
                name=name+line[i]
            if (line[i]).isdigit()==True:
                mark=mark+line[i]
        surnames.append(name)         #add name to surnames 
        percentage.append(mark)       #add mark to pecentages 
    f.close()                               #close file
    
    
    dropout= average(percentage)-stand_dev(percentage)   #find mark for which peopld need to see advisor
    
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