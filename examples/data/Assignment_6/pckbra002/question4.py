"""program that takes in a list of marks and then makes a histogram representation of the marks according to UCT's mark categories"""
#Bandon Pickup (PCKBRA002)
#2014/04/22
#Assignment 6 Question 4

marks = input("Enter a space-separated list of marks:\n").split(" ")
categories={"1":0,"2+":0,"2-":0,"3":0,"F":0}#Mark categories according to UCT
for mark in marks:#runs through every mark in the list of marks and adds a unit to the category that the mark falls within
    if int(mark)>=75:
        categories["1"] +=1
    elif int(mark) >=70:
        categories["2+"] +=1
    elif int(mark) >=60:
        categories["2-"] +=1
    elif int(mark) >= 50:
        categories["3"] +=1
    else:
        categories["F"] +=1
print("1 |","X"*int(categories["1"]),sep="")#prints a hard coded axes with a histogram, 'X' is repeated however many times their are marks in that particular category
print("2+|","X"*int(categories["2+"]),sep="")
print("2-|","X"*int(categories["2-"]),sep="")
print("3 |","X"*int(categories["3"]),sep="")
print("F |","X"*int(categories["F"]),sep="")