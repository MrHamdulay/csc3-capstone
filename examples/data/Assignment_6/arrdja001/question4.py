"""Assignment 6 Question 4
25 April 2014
Djavan Arrigone"""

marks = input("Enter a space-separated list of marks: \n")
splitm = marks.split(" ")
mlist = []

for i in splitm: #appends evalled values to mlist.
    num = eval(i)
    mlist.append(num)

F = 0
three = 0
twom = 0
twop = 0
one = 0

for j in mlist: # conditional loop which add values to groups according to marks. 
    
    if j < 50:
        F += 1
    elif j >= 50 and j<60:
        three += 1  
    elif j >= 60 and j<70:
        twom += 1  
    elif j >= 70 and j<75:
        twop += 1 
    else: one += 1

print("1 |" + "X"*one)
print("2+|" + "X"*twop)
print("2-|" + "X"*twom)
print("3 |" + "X"*three)
print("F |" + "X"*F)
    
