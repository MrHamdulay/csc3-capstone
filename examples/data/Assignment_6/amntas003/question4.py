#AMNTAS003  #Tashfia Amin   #Due date: 25 April 2014
#Question 4: Assignment 6   #List of marks in histogram form

#Input list of marks
points = input("Enter a space-separated list of marks:\n")

#Create a list from the input of marks
marks=points.split(" ")

#Create variables for each case
First = 0
UpperSecond = 0
LowerSecond = 0
Third = 0
Fail = 0

#Keep count of number of marks
for i in marks:
    if eval(i) >= 75:
        First = First + 1
    elif 75 > eval(i) >= 70 :
        UpperSecond = UpperSecond + 1 
    elif 70 > eval(i) >= 60 :
        LowerSecond = LowerSecond + 1
    elif 60 > eval(i) >= 50 :
        Third = Third + 1
    else:
        Fail = Fail + 1

#Print a histogram
print("1 |", "X"*First, sep="")
print("2+|", "X"*UpperSecond, sep="")
print("2-|", "X"*LowerSecond, sep="")
print("3 |", "X"*Third, sep="")
print("F |", "X"*Fail, sep="")