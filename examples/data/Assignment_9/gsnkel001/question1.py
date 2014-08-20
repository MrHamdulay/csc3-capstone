"""student adviser
Kelly Goosen
2014/05/10"""



import math

def average (marks):
    
    """"calculates average of a list"""
    
    total = 0
    for i in range(len(marks)):#converts marks to list
        total = total + int(marks[i])
    return (total/len(marks)) #two decimal places




def stand_dev (values):
    
    """calculate standard deviation of values"""
    
    mean = average(values) #calculates the average of the marks
    total=0  #initialise  variable
    for i in range(len(values)):
        total = total+(mean - int(values[i]))**2
    variance=total/(len(values)) #variance = standard deviation squared 
    return (math.sqrt(variance))




def main ():
    
    x = input("Enter the marks filename:\n") # get input from user
    surnames = []
    percentage = []
    f = open(str(x), "r") #open file
    for line in f:  #iterates through each line in file
        name = ""
        mark = ""
        for i in range (len(line)): #iterate through each character in file
            if (line[i]).isalpha () == True:
                name = name + line[i]
            if (line[i]).isdigit () == True:
                mark = mark + line[i]
        surnames.append (name)  #add names  
        percentage.append (mark) #add marks
    f.close()  
    
    
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