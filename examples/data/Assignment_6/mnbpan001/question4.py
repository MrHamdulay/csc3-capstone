""" Program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks
Pankaj Munbodh
20 April 2014"""
#Create dictionary of marks from list of marks
marks1=input("Enter a space-separated list of marks:\n").split()
marks_l=[]
for j in marks1:    #converting each string in list to a number
    marks_l.append(eval(j))
marks_d={}
for i in range(len(marks_l)):
    count=marks_l.count(marks_l[i])
    if (marks_l[i] in marks_d) == False:
        marks_d[marks_l[i]]=count

#Creating list of keys from dictionary of marks
marks2=list(marks_d.keys())

#Initialising variables
number_first=0
number_uppersecond=0
number_lowersecond=0
number_third=0
number_f=0
#Checking in which range mark(key) fits.
for mark in marks2:
    if mark >= 75:
        number_first+=marks_d[mark]
    elif 70<=mark<75:
        number_uppersecond+=marks_d[mark]
    elif 60<=mark<70:
        number_lowersecond+=marks_d[mark]
    elif 50<=mark<60:
        number_third+=marks_d[mark]
    else:
        number_f+=marks_d[mark]
#Output the number of marks found within each category as a histogram       
print("1","|"+"X"*number_first)
print("2+","|","X"*number_uppersecond,sep='')
print("2-","|","X"*number_lowersecond,sep='')
print("3","|"+"X"*number_third)
print("F","|"+"X"*number_f)
        
#This program classifies marks into keys first and then checks to see within which class each key fits
#and adds the respective value of each key to obtain the total number of marks within a class