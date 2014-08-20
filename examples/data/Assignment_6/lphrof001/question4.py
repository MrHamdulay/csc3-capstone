"""Program that takes in a list of marks
Author: Rofhiwa Liphauphau
Date: 23 April 2014"""
marks=input("Enter a space-separated list of marks:\n")
marks=marks.split(" ")
fail=0
third=0
lower_second=0
upper_second=0
first=0 #creating variables
for mark in marks: #sorting the input into the different categories
    if int(mark) >=75:
        first+=1
    elif 70<=int(mark)<75:
        upper_second+=1
    elif 60<=int(mark)<70:
        lower_second+=1
    elif 50<=int(mark)<60:
        third+=1
    else:
        fail+=1
print("1 |"+first*"X")
print("2+|"+upper_second*"X")
print("2-|"+lower_second*"X")
print("3 |"+third*"X")
print("F |"+fail*"X")
