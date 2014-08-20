#Histogram representation of marks
#Jennifer Yuan
#23 April 2014

A = input("Enter a space-separated list of marks:\n") #gets marks from user

one = [] #empty strings
twoplus = []
twominus = []
three =[]
F = []

marks = A.split(" ") #separates items into list of strings

x=0
for i in marks: #converts strings to numbers to do arithmetic
    y = eval(i)
    marks[x] = y #replacing strings with number equivalent
    x=x+1 #accumulator variable

for i in marks:
    if i>= 75: #separates marks into categories and adds "X" to each respective list if mark is in that category
        one.append("X")
    elif i>=70:
        twoplus.append("X")
    elif i>=60:
        twominus.append("X")
    elif i>=50:
        three.append("X")
    else:
        F.append("X")

print("1 |", "X" * len(one), sep="") #prints histogram and "X" according to how many items in each respective list. 
print("2+|", "X" * len(twoplus), sep="")
print("2-|", "X" * len(twominus), sep="")
print("3 |", "X" * len(three), sep="") 
print("F |", "X" * len(F), sep="") 
        