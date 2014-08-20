#Question 1
#Determining students needing to see a student advisor.
#By: Dean de Haast

import math
filename=input("Enter the marks filename:\n")
f= open(filename, "r")  #Opening the file
student_array = f.readlines() #writing the file into an list
mark_array =[]
advisor=[]
f.close() # Closing the file once done with it
      

def checking(student_array):
    total = 0  
    average = 0
    deviation = 0
    #Filling a list with the names and marks + calculating the average
    for i in range (len(student_array)):
        mark_array.append(student_array[i].split(","))       
        total+= eval(mark_array[i][1])
        
    average = total/len(student_array)
    #Calculating std deviation    
    for x in range (len(student_array)):
        deviation += (eval(mark_array[x][1])- average)**2
        
    deviation = math.sqrt(deviation/len(student_array))
    
    print("The average is:", "%0.02f" % average)
    print("The std deviation is:", "%0.02f" % deviation)
    
    #Finding students below min requirement
    for y in range (len(student_array)):
        if eval(mark_array[y][1]) + deviation < average:
            advisor.append(mark_array[y][0])
    
    advisor.append("")
    #Incase no one needs advisor        
    if advisor[0] != "":
        advisor.remove("")
        print("List of students who need to see an advisor:")
        for x in advisor:
            print(x)
        
               
checking(student_array)