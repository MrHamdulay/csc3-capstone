"""question 4-assignment 6- counting mark grades and formulating histogram
GVNPRI022
23 April 2014"""
marks= input("Enter a space-separated list of marks:\n").split(" ") #inputting a list
for i in range (len(marks)): #evaluating a list
    marks[i]=eval(marks[i])
#initialising counters
no1=0
no2plus=0
no2minus=0
no3=0
noFail=0
#checking mark category
for j in range(len(marks)):
    if (marks[j]<50):
        noFail=noFail+1
    elif(50<=marks[j]<60):
        no3=no3+1
    elif(60<=marks[j]<70):
        no2minus=no2minus+1
    elif(70<=marks[j]<75):
        no2plus=no2plus+1
    else:
        no1=no1+1
#outputting histogram
print("1 |"+(no1*"X"))
print("2+|"+(no2plus*"X"))
print("2-|"+(no2minus*"X"))
print("3 |"+(no3*"X"))
print("F |"+(noFail*"X"))
