# question4.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 23 April 2014

marks=input("Enter a space-separated list of marks:\n")

marks_list=marks.split(" ")                                 #split marks into list

#create empty string
first=""                          
upper_second=""
lower_second=""
third=""
fail=""

#loop through entered marks to create bars
for i in marks_list:
    m=eval(i)
    if m>=75:
        first+="X"
    elif m>=70:
        upper_second+="X"
    elif m>=60:
        lower_second+="X"
    elif m>=50:
        third+="X"
    else:
        fail+="X"

#print histogram
print("1 |"+first)
print("2+|"+upper_second)
print("2-|"+lower_second)
print("3 |"+third)
print("F |"+fail)