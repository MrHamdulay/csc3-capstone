#program to analyse student marks read in from a file and determine which students need to see a student advisor
#KNNSAD001
#Assignment 9

import math

filename=input("Enter the marks filename:\n")        
f = open(filename,"r")
lines=f.readlines()                     #opens file and reads data- puts each string in each line into an individual list
marks=[]
names=[]
mean_mark=0

for i in range(len(lines)):
    marks.append(lines[i].split(',')[1].split("\n")[0])
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    mean_mark+=marks[i]                     #to find the mean mark per student by spiliiting the individual marks in the lists and calculating mean
    
mean_mark=mean_mark/len(marks)
s_deviation=0

for i in range(len(marks)):
    s_deviation+=(marks[i]-mean_mark)**2
s_deviation=math.sqrt(s_deviation/len(marks))                   #uses the calculated mean mark above to calculate std deviation
                                                            
print("The average is:","{:.2f}".format(mean_mark))
print("The std deviation is:","{:.2f}".format(s_deviation))
advsr=False

for i in range(len(marks)):
    if(marks[i]<(mean_mark-s_deviation)):                 #if mark is below bthe average mark = student needs a student advisor)
        advsr=True
        
if(advsr):
    print("List of students who need to see an advisor:")              #prints students who need to see an advisor based on marks
    for i in range(len(marks)):
        if(marks[i]<(mean_mark-s_deviation)):                        
            print(names[i])
