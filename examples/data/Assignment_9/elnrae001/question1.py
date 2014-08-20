'''Program to analyse student marks read in from a file and determine which students need to see a student advisor.
Author:Raees Eland
Date:10 May 2014'''
import math

filename=input('Enter the marks filename:\n')
f=open(filename,'r')
lines=f.readlines() 
f.close()

# creates a list of names and list of marks
list_of_names=[]
list_of_marks=[]
for line in lines:
    position = line.find(',')
    list_of_names.append(line[:position]) #list of only the names
    list_of_marks.append(line[position+1:]) #list of only the marks
    
# calculates the average   
total_marks = 0 
for i in list_of_marks:
    total_marks+=int(i)
average = round(total_marks/len(list_of_names),2) #calculates the mean
if average == int(average):
    average = str(total_marks/len(list_of_names))+'0' #if decimal=.00
print('The average is:',average)
    
#calculates standard deviation
std2=0
for mark in list_of_marks:
    std2+=(int(mark)-float(average))**2
std=round(math.sqrt(std2/len(list_of_marks)),2)
if std==0.0:
    print('The std deviation is: 0.00')
else:
    print('The std deviation is:',std)


#student who must see advisor
if std!=0:
    print('List of students who need to see an advisor:')
    one_std=float(average)-std
    for j in range(len(list_of_marks)):
        if int(list_of_marks[j]) < one_std:
            print(list_of_names[j])
        
     
     
                   

    

    

    
