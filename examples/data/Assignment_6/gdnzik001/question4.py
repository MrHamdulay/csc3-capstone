"""program to catagorise a list of marks entered by the user
Zikho Godana
25 April 2014"""

mark=input("Enter a space-separated list of marks:\n")

grades=["F","3","2-","2+","1"]
#grades=[]


#store the marks as a list
marks=mark.split()
#create an empty counter
counter={}
for mark in marks:
    #classify the marks into grades
    if int(mark)<50:
        grade="F"
    elif 50<=int(mark)<60:
        grade="3"
    elif 60<=int(mark)<70:
        grade="2-"
    elif 70<=int(mark)<75:
        grade="2+"
    elif int(mark)>=75:
        grade="1"
    #print(mark,grade)
    #grades.append(grade)
    
    #count grades and add new grades as they are counted
    if grade not in counter:
        counter[grade]=1
    else:
        counter[grade]+=1

        
output="{0:<2}|{1:>1s}"
for grade in sorted(grades):
    if grade not in counter:
        print(output.format(grade,0*"X"))
for grade in sorted(counter):
    print(output.format(grade,counter[grade]*"X"))
    
           
    