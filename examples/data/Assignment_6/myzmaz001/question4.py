""" Program to represent marks according to UCT mark categories as a histogram
Mazwi Myeza
21 April 2014
Assignment6
Question4
"""
#Asking user to enter marks and setting up tracer variables
results = input("Enter a space-separated list of marks:\n")
mark = results.split(" ")
marks = []
fail = 0
third = 0
lower2nd = 0
upper2nd = 0
first = 0
#Populating array with marks 
for i in range(len(mark)):
    marks.append(eval(mark[i]))
#Categorising marks and increasing appropriate category tracers    
for j in range(len(marks)):
    if marks[j] >= 75:
        first += 1
    elif marks[j] >= 70:
        upper2nd += 1
    elif marks[j] >= 60:
        lower2nd += 1
    elif marks[j] >= 50:
        third += 1
    else:
        fail += 1
#printing out the histogram using variable(category) tracers        
print("1 |"+first*"X")   
print("2+|"+upper2nd*"X")
print("2-|"+lower2nd*"X")
print("3 |"+third*"X")
print("F |"+fail*"X")

    