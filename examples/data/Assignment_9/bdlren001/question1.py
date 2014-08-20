# A python program to analyse student marks read in from a file and determine which students need to see a student advisor.
# Budeli Rendani
# BDLREN001
# 13/05/2014

import math # importing the math from library
def main():
    x=input("Enter the marks filename:\n") # Obtaining input from the user
    infile=open(x,"r") # reading the file that was requested
    
    sum_values=0 # setting the sum to 0
    count=0 # Setting the count to 0 for counting the number of lines in the file
    std=0 # accumulator for the mean-score values
    score_list=[] # making a list for the scores
    score_name=[] # making a list for the scores with the names
    
    for i in infile:
        name, score = i.split(",") # In each line the name and score are seperated by comma
        score=eval(score) # converting score to a number
        sum_values+=score # adding score to the accumulator
        count+=1 # adding the counts to the accumulator
        score_list.append(score) # appending score to the list
        score_name.append(i) #appending score and name to the name
        
    
    y=sum_values/count  # calculating the mean
    for i in score_list:
        std+=(y-i)**2  # adding mean-score to the accumulator
     
    v=math.sqrt(std/count) # calculating the final standard deviation
    print("The average is:","%.2f"%(y))# printing out rounded mean
    print("The std deviation is:","%.2f"%(v)) # printing out rounded standard deviation
    

    names_2=[] # Empty list for students who need to see a tutor
    for i in score_name:
        name,score=i.split(",") # name and score splited by comma in the list
        if int(score)< y-v:# print out the name of the student who needs to see an advisor
            names_2.append(name) # appending the names of students who need to see a tutor to the empty list
    if names_2==[]: # Nothing should be printed if the list is still empty
        return  
    else:   
        print("List of students who need to see an advisor:") # printing out title of names of students who performed below 1 standard deviation of the mean    
    
    for i in names_2:
        print(i) #print out the names in the list
                
main()      
    