"""Amy Bosworth, Assignment 6, Question 4, program that takes in a list of marks and outputs a histogram"""

#Get mark list
marks=input("Enter a space-separated list of marks:\n")
marks=marks.split()

# set grades to 0
fail=0
third=0
usecnd=0
lsecnd=0
first=0

#loop through mark list, identify mark into a class
for i in marks:
    if eval(i)<50:
        fail+=1
    elif 50<=eval(i)<60:
        third+=1
    elif 60<=eval(i)<70:
        usecnd+=1
    elif 70<=eval(i)<75:
        lsecnd+=1
    elif eval(i)>=75:
        first+=1
        
#print histogram        
print("1 |",first*'X',sep='')
print("2+|",lsecnd*'X',sep='')
print("2-|",usecnd*'X',sep='')
print("3 |",third*'X',sep='')
print("F |",fail*'X',sep='')

        
        
        
