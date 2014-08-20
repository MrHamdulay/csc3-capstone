'''Q4 of Assignment 6: Program to create histogram from mark data
Patrick Boroughs
21 April 2014'''

#Input values and create an array, seperated by spaces
marks=input("Enter a space-separated list of marks:\n").split(' ')

#Create categories array for 2d counting
categories=[0,0,0,0,0]

#loop through array and test which category mark falls under
for i in range(len(marks)):
    if eval(marks[i])<50: #F
        categories[0]+=1
    elif eval(marks[i])<60: #3
        categories[1]+=1
    elif eval(marks[i])<70: #2-
        categories[2]+=1
    elif eval(marks[i])<75: #2+
        categories[3]+=1
    else:                   #1
        categories[4]+=1
    
#print results
print("1 |",categories[4]*'X',sep='')
print("2+|",categories[3]*'X',sep='')
print("2-|",categories[2]*'X',sep='')
print("3 |",categories[1]*'X',sep='')
print("F |",categories[0]*'X',sep='')