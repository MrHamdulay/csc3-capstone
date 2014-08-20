"""Assignment 6, question 4:Creates a histogram for the marks from a list of marks
Dean Gracey
23 April 2014"""

marks = input("Enter a space-separated list of marks:\n").split(" ")

fail = 0
third =0
lower2 = 0
upper2 = 0
first = 0

for mark in marks:
    
    if (int(mark)>=0 and int(mark) <=100):
        if (int(mark)<50):
            fail +=1
        
        elif (int(mark)<60):
            third +=1
        
        elif (int(mark)<70):
            lower2 +=1
        
        elif (int(mark)<75):
            upper2 +=1
        else:
            first +=1
            
print("1 |"+"X"*first)
print("2+|"+"X"*upper2)
print("2-|"+"X"*lower2)
print("3 |"+"X"*third)
print("F |"+"X"*fail)

    