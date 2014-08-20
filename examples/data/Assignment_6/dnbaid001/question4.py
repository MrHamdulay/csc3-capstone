#Assignment 6 - Question 4
#Histogram
#Author: Aidan de Nobrega DNBAID001
#19/04/2014

marksinput = input("Enter a space-separated list of marks:\n")

list_of_marks= marksinput.split() #converts marksinput to a list of strings
list_of_marks = [int(x) for x in list_of_marks] #Makes each element in list an int

firsts = 0
high_seconds = 0
low_seconds = 0
thirds = 0
fails = 0

for mark in list_of_marks: #categorises marks.
    if 75 <= mark <= 100:
        firsts += 1 #Only necessary to increment range. Exact numbers voided
    elif mark >= 70:
        high_seconds += 1
    elif mark >= 60:
        low_seconds += 1
    elif mark >= 50:
        thirds += 1
    else:
        fails += 1
    
print("1 |" + "X"*firsts)
print("2+|" + "X"*high_seconds)
print("2-|" + "X"*low_seconds)
print("3 |" + "X"*thirds)
print("F |" + "X"*fails)

        
