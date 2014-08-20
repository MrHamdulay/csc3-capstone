"""Akhil Singh
SNGAKH004
Program to draw a histogram of class mark data.
23 April 2014"""

#Get class marks from user
class_mark=input("Enter a space-separated list of marks:\n")

#Converting a string into a list of intergers
class_mark=class_mark.split()
for a in range(len(class_mark)):
    class_mark[a]=eval(class_mark[a])
    
#Specifying acumulators for variables    
first = 0
upper_second = 0
lower_second = 0
third = 0
fail = 0
        
        
#Determining the place of marks        
for m in class_mark:
    if m >= 75:
        first = first +1
    elif m >= 70:
        upper_second =upper_second + 1
    elif m >= 60:
        lower_second =lower_second+ 1
    elif m >= 50:
        third=third + 1
    else:
        fail=fail+ 1

#Print histogram.
print("1 |", "X"*first, sep = "")
print("2+|", "X"*upper_second, sep = "")
print("2-|", "X"*lower_second, sep = "")
print("3 |", "X"*third, sep = "")
print("F |", "X"*fail, sep = "")
