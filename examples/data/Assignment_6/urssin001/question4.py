'''Write a program that takes in a list of marks (separated by spaces) and 
   outputs a histogram representation of the marks according to the mark categories at UCT:
            fail < 50%
            50% <= 3rd < 60%
            60% <= lower 2nd < 70%
            70% <= upper 2nd < 75%
            1st >= 75%
Sinead Urisohn
19 April 2014
'''
#get grades
grades=input("Enter a space-separated list of marks:\n")
#split grades into array
gradeSplit=grades.split()

#set variables to count each grade category to print histogram
fail=""
third=""
lower2=""
upper2=""
first=""

#loop through array
#use if statements to determine grade category accordint to UCT system

for grade in range(len(gradeSplit)):
    #get value of each grade to compare numbers
    gradeValue= int(gradeSplit[grade])
    if gradeValue>=75:
        first+="X"
    
    elif gradeValue>=70:
        upper2+="X"
    elif gradeValue>=60:
        lower2+="X"
    elif gradeValue>=50:
        third+="X"
    else:fail+="X"
#print histogram
print("1 |"+first+"\n2+|"+upper2+"\n2-|"+lower2+"\n3 |"+third+"\nF |"+fail)