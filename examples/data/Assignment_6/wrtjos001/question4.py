"""Assignment 6 Question 4 histogram reprentation of marks
joshua wort
20 april 2014"""

#get list of marks
mark=input("Enter a space-separated list of marks:\n")
marks=mark.split(" ")

#variables
F=""
third=""
lower_second=""
upper_second=""
first=""

#sort marks into categories
for mark in marks:
    if eval(mark)<50:
        F+="X"
    elif eval(mark)<60:
        third+="X"
    elif eval(mark)<70:
        lower_second+="X"
    elif eval(mark)<75:
        upper_second+="X"
    else:
        first+="X"
#print histogram
print("1 |",first,sep="")
print("2+|",upper_second,sep="")
print("2-|",lower_second,sep="")
print("3 |",third,sep="")
print("F |",F,sep="")
