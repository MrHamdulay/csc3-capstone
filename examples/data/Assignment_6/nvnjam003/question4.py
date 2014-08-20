#James Nevin
#Assignment 6, Question 4
#23/04/2014

marks = input("Enter a space-separated list of marks:\n").split() #Marking list of marks
ranks = [0, 0, 0, 0, 0] #Number for each
for x in range (len(marks)):
    mark = int(marks[x]) #Temp variable for int operation
    if (mark < 50): #Checking which category
        ranks[0] += 1
    elif (50 <= mark < 60):
        ranks[1] += 1
    elif (60 <= mark < 70):
        ranks[2] += 1
    elif (70 <= mark < 75):
        ranks[3] += 1
    else:
        ranks[4] += 1

if marks:
    for x in range (4, -1, -1): #Moving backwards through list
        if (x == 4): #Printing headers
            print ("1 |", end = "")
        elif (x == 3):
            print ("2+|", end = "")
        elif (x == 2):
            print ("2-|", end = "")
        elif (x == 1):
            print ("3 |", end = "")
        else:
            print ("F |", end = "")
        print (ranks[x]*"X") #Printing total of each
        
        