#program to enter marks and output graph of results
#michael field
#21 april 2014

input1 = input("Enter a space-separated list of marks:\n")

marks = input1.split()
count1st = 0
count2up = 0
count2low = 0
count3 = 0
countF = 0

#divide marks up into categories
for i in range(len(marks)):
    
    #1st
    if eval(marks[i]) >= 75:
        count1st += 1
    
    #2nd upper
    elif eval(marks[i]) >= 70:
        count2up += 1
    
    #2nd lower
    elif eval(marks[i]) >= 60:
        count2low += 1
        
    #3rd
    elif eval(marks[i]) >= 50:
        count3 += 1
        
    #fail increase by one
    else:
        countF += 1
    
#print marks and graph
print("1 |", 'X' * count1st, sep="")
print("2+|", 'X' * count2up, sep="")
print("2-|", 'X' * count2low, sep="")
print("3 |", 'X' * count3, sep="")
print("F |", 'X' * countF, sep="")