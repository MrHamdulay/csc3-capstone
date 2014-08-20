""" program to analyse student marks read in from a file and determine which students need to see a student advisor
JP Lanser
11 May 2014"""

file_name = input("Enter the marks filename:\n")

f = open(file_name, 'r')


list_of_students = f.readlines()
f.close()

count= 0 #count to keep track of the position in the list
for i in list_of_students: #Get rid of the newline '\n' at the end of each entry 
    if '\n' in i:
        list_of_students[count] = list_of_students[count][:-1]
    count+=1
        
    
#Create an empty dictionary to store names, corresponding with marks.


dictionary={}  

for name_and_mark in list_of_students:    
    temporary_list = name_and_mark.split(',') #Now split the student and his/her mark so that they can be added into a dictionary 
    
    dictionary[temporary_list[0]]= temporary_list[1]
    
total_marks = 0
count =0 
#Now add up all the marks (loop through dictionary), keep a count so that mean can be determined

for i in dictionary:
    count+=1
    mark = eval(dictionary[i])
    total_marks+=mark
    
mean = total_marks/count #calcuate mean

#Now loop through dctionary, and work out the variance. Then calculate standard deviation (sqrt(variance))
variance =0
for i in dictionary:
    mark = eval(dictionary[i])
    variance+= ((mean - mark)**2)


import math   
    
standard_deviation = math.sqrt(variance/count)

average = '{0:^4.2f}'.format(mean) #format to two decimals as required
std_deviation = '{0:^4.2f}'.format(standard_deviation)

print('The average is:', average)
print('The std deviation is:', std_deviation)

#Now create a list to check which students are below one standard deviation of the mean. Loop through dictionary
list_for_advisor=[]
for i in dictionary:
    if eval(dictionary[i]) < (mean - standard_deviation):
        list_for_advisor.append(i)
        
        
#Now print those who need to see the advisor, need to be printed in the order that the names appeared in the original text file


if not list_for_advisor==[]:
    print("List of students who need to see an advisor:")
    for i in list_of_students:  #loop through original order of text file
        x = i.split(',') #split at the comma, the name will be the first entry of the list
        if x[0] in list_for_advisor:
            print(x[0])
            
        
        
        
   
        
        

        








    


    





        