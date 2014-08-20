# Dalise Steynfaard
# STYDAL001
# Assignment 1, question 2
# 04-03-2014

t = ""
h = eval(input("Enter the hours:\n"))
m = eval(input("Enter the minutes:\n"))
s = eval(input("Enter the seconds:\n"))

if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        t = "Your time is valid."
else:
        t = "Your time is invalid."
    
print(t)