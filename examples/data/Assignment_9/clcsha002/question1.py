"""assignment 9 question 1
shannon clacey 
13 may 2014"""
 
import math

def std_deviation(): 
    
    filename = input("Enter the marks filename:\n") #gets input from user on what file to use
    f = open(filename, 'r') #allows the file to be read
    marksstring = f.read() #reads the file into one long string
    f.close() #close the file
    
    marksarray = [] #create empty string for which to add marks
    array2 = [] #list containing marks and names, items separated by the comma
    array1 = [] #creats array which will be split at the end of each line to create a string with each item being a new person and their mark
    array1 = marksstring.split("\n")    
    
    total = 0 #establishing starting values of variables to be used for ease
    counter = 0
    std_dev = 0
    
    for line in array1:
        array2.append(line.split(",")) #appending the array by adding the names and marks separated by a comma
    
    for loop in range(0,len(marksstring)+1):
        if marksstring[loop:loop+1] == ",":
            mark = marksstring[loop+1:loop+3]
            marksarray.append(int(mark))
            total += int(mark) #this counts the total summation of the marks
            counter += 1 #counts the number of people involved
    
    ave = total/counter #calculates average and rounds to two decimal places
    ave_round = round(total/counter, 2)
    
    for a in marksarray:
        std_dev += (int(a)-ave)**2 #initiate standard deviation calculation    
    
    std_dev = math.sqrt(std_dev/counter) #calculates standard deviation and rounds to 2 decimal places
    std_round = round(std_dev,2)
    
    ave_round = str(ave_round) #converts standard deviation and average to string
    finalstd = str(std_round)
    
    for b in range(0,len(finalstd)): #assignment of random variable for ease
        if (finalstd[b] == ".") and (finalstd[b+1:] == "0"):
            finalstd = finalstd+"0" #formats additional 0 to be added where necessary
            
    for c in range(0,len(ave_round)):
        if (ave_round[c] == ".") and (ave_round[c+1:] == "0"):
            ave_round = ave_round+"0" #further formatting of adding 0 where necessary (i.e. rounding does not give 2 decimal places)
            
    namesarray = [] #create empty array to which names will be added
    advisor = ave - std_dev #sees if student should potentially see student advisor
    boolean = False
    
    for d in range(len(array2)-1): #random assignment of variable d 
        if eval(array2[d][1]) < advisor: #checking which students need to see the addvisor
            boolean = True
            namesarray.append(array2[d][0])
    
    print("The average is:", ave_round)
    print("The std deviation is:", finalstd)
    
    if boolean == True:
        print("List of students who need to see an advisor:")
        for e in namesarray: #prints the students needing to see the advisor 
            print(e)
std_deviation()
    
        
    
    
                                  
    
        
           
       
       
        
    
    
        

        
    




            
    
    
    