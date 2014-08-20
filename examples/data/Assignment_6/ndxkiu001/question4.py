#Kiuran Naidoo
#Assignment 6
#Question 4
#24 April 2014

inputMarks = input("Enter a space-separated list of marks:\n").split(" ") #Get input from user
for x in range (len(inputMarks)):
    inputMarks[x] = eval(inputMarks[x]) #Convert input from strings to integers
markBreakdown =[0,0,0,0,0] #List for storing mark category counts

for x in range(len(inputMarks)):
    if inputMarks[x] >= 75: #Checking mark ranges and then updating the categories
        markBreakdown[0] = markBreakdown[0]+1
    elif inputMarks[x] <75 and inputMarks[x] >= 70:
        markBreakdown[1] = markBreakdown[1]+1
    elif inputMarks[x] <70 and inputMarks[x] >=60:
        markBreakdown[2] = markBreakdown[2]+1
    elif inputMarks[x] <60 and inputMarks[x] >=50:
        markBreakdown[3] = markBreakdown[3] +1
    else:
        markBreakdown[4] = markBreakdown[4]+1

#printing the histogram
print("1 |","X"*markBreakdown[0],sep="")
print("2+|","X"*markBreakdown[1],sep="")
print("2-|","X"*markBreakdown[2],sep="")
print("3 |","X"*markBreakdown[3],sep="")
print("F |","X"*markBreakdown[4],sep="")
