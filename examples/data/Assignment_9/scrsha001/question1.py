#Shaaheen Sacoor SCRSHA001
#13 May 2014
#Program to work out average and standard deviation from marks given by a document and see who is below one std dev.

import math
def main():
    filename = input("Enter the marks filename:\n")    #Gets file
    f= open(filename,"r")
    input_list = f.readlines()                           # Reads lines of document
    split_list =[]
    for j in range(len(input_list)):
        split_list = split_list + input_list[j].split(",")   #Splits names and marks and adds both to a list
    marks =[]
    names =[]
    for i in range(0,len(split_list),2):           #Splits names and marks to different list
        marks.append(eval(split_list[i+1]))        #Marks are the odd number in the list, hence [i+1]
        names.append(split_list[i])

    sumL = 0
    for i in range(len(marks)):          #Adds all marks together
        sumL+=marks[i]
    
    average = sumL/(len(marks))          #Works out and average and prints it
    print("The average is:",'{:.2f}'.format(average))

    sumD= 0
    for i in range(len(marks)):                     #Working out for std deviation
        sumD += (marks[i]-average)**2
    
    std_dev = round(math.sqrt((sumD)/(len(marks))),2)     
    print("The std deviation is:",'{:.2f}'.format(std_dev))
    
    
    for i in range(len(marks)):
        if marks[i]<(average-std_dev):          #If a mark is under one std dev, then print this
            print("List of students who need to see an advisor:")
            break
        
    for i in range(len(marks)):              #Prints people under one std dev
        if marks[i]<(average-std_dev):         
            print(names[i])
    f.close()
main()