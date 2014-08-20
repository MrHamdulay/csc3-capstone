"""BLLKAT005
Kate Bell
12 May 2014
Assignment 9 Q1"""

import math

def round_two(x):
    x = round(x,2)
    if str(x).endswith(".0"):
        return str(x)+"0"
    else:
        return str(x)

# read names and marks from file into a list
markslist = []
filename = input("Enter the marks filename:\n")
f = open(filename,'r')
for line in f:
    markslist.append(line.split(","))
f.close()

#get rid of '\n' at end of mark and make marks into integers 
for i in range (len(markslist)):
    if markslist[i][1].endswith("\n"):
        markslist[i][1]=markslist[i][1][:-1]
    markslist[i][1]=eval(markslist[i][1])
    
#find average 
total = 0
for j in range (len(markslist)):
    total += markslist[j][1]
average = total/len(markslist) 
print("The average is:",round_two(average))

#find standard deviation 
squared_totals = 0
for k in range(len(markslist)):
    squared_totals += (markslist[k][1]-average)*(markslist[k][1]-average)
stan_dev = math.sqrt(squared_totals/len(markslist))
print("The std deviation is:",round_two(stan_dev))

#check if there are students who need advisor 
need = False
for l in range (len(markslist)):
    if markslist[l][1]< (average-stan_dev):
        need = True

#Print list of students who need advisor
if need == True:
    print("List of students who need to see an advisor:")
    for l in range (len(markslist)):
        if markslist[l][1]< (average-stan_dev):
            print(markslist[l][0])