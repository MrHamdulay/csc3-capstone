"""Aiden Walton
WLTAID001
Assignment 6 - Question 4"""

raw_input=input("Enter a space-separated list of marks:\n")
markstemp=raw_input.split(" ")
fail=0
third=0
lsecond=0
usecond=0
first=0
for mark in markstemp:
    mark=int(mark)
    if mark<50:
        fail+=1
    elif 50<=mark<60:
        third+=1
    elif 60<=mark<70:
        lsecond+=1
    elif 70<=mark<75:
        usecond+=1
    elif mark>=75:
        first+=1
        
print("1 |", "X"*first,sep="")
print("2+|", "X"*usecond,sep="")
print("2-|", "X"*lsecond,sep="")
print("3 |", "X"*third,sep="")
print("F |", "X"*fail,sep="")