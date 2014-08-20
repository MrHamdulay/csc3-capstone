"""create a histogram of test scores
   Rivoningo Seweya
   23 April 2014"""
# ask user for a list of scores
scores=input("Enter a space-separated list of marks:\n")
score=scores.split(" ")
#create an empty mark list
marks = {}
#set string variables
y=0
a=0
b=0
c=0
d=0
#seperate marks
for mark in score: 
    x=eval(mark)
    if x>=75:
        marks[mark]= 1
        y+=(marks[mark])
    elif 75>x>=70:
        marks[mark]=1
        a+=(marks[mark])
    elif 70>x>=60:
        marks[mark]=1
        b+=(marks[mark])
    elif 60>x>=50:
        marks[mark]=1
        c+=(marks[mark]) 
    else:
        marks[mark]=1
        d+=(marks[mark])  
print("1 |"+"X"*y,"\n2+|"+"X"*a,"\n2-|"+"X"*b,"\n3 |"+"X"*c,"\nF |"+"X"*d)