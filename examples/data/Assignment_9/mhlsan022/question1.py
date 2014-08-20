'''This program analyses student marks read in from a file and determine which students need to see a student advisor.
Sandile Christopher Mahlangu
12 May 2014'''

import math
def marks_file():
    '''This function read marks from a file, calculates the average marks, the standard deviation and determines which students need to see a student advisor'''
    filename=input("Enter the marks filename:\n")
    marksheet=open(filename,'r')   #opening the file 
    data=marksheet.readlines() #making an array of the data in the file
    marksheet.close()#closing the file
    
    new_data=[]#Marks and student in a 2d array
    
    for string in range(len(data)):
        #This loop is to remove the trailing new line character 
        if data[string][-1]=='\n':
            data[string]=data[string][:-1]
   
    for new in range(len(data)):
        #make the data in to a double array by appendng it to the new_data array
        new_data.append(data[new].split(','))#appanding the student and their marks as a list
    
    
    data_dict={} #A dictionary to keep students as a key and marks as a value
    for marks in range(len(new_data)):
        #This loop is to evaluate the marks and add the data into a dictionary contaning a student as a value and a mark as a key
        data_dict[eval(new_data[marks][1])]= new_data[marks][0]
    
    marks_array=[]  # A list that will only have marks 
    for mark in range (len(new_data)):
        #Adding the marks to the array
        marks_array.append(eval(new_data[mark][1]))
    
    
    
    #Calculating the average of the marks which is the sum of the marks over the number of marks
    
    mark_sum=0
    mark_number=len(marks_array)
    for add in range(len(marks_array)):  #Summing the marks
        mark_sum+=marks_array[add]
    average=mark_sum/mark_number
    
    print('The average is: {0:.2f}'.format(average))
    
    #Calculating the standard deviation. 
    
    #First I'll calculate the difference of each data point from the mean (Calling it point), and square the result of each then add them
    point=0
    for the_mark in range(len(marks_array)):
        point+=(marks_array[the_mark]-average)**2
    
    #Then divide the point by the number of marks and take the square root
    standard=math.sqrt(point/mark_number)
    
    print('The std deviation is: {0:.2f}'.format(standard))
    
    #Now for the students who need to see an advisor, the ones below one standard deviation of the mean
   
    below_mean= average-standard
    
    for a_mark in range(len(marks_array)):
            if marks_array[a_mark]<below_mean:    #Checking if there's a student who needs to seen an advisor
                print('List of students who need to see an advisor:')
                break
    #moving along the marks and printing out the value(student) who got below
    for a_mark in range(len(marks_array)):
        if marks_array[a_mark]<below_mean:
            print(data_dict[marks_array[a_mark]])
        
if __name__=='__main__':
    marks_file()