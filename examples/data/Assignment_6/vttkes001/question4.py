"""Histogram Representation
Keshin Vittee
25 April 2014"""
marks = input("Enter a space-separated list of marks:\n").split(" ")
grade = {"1 ":0,"2+":0,"2-":0,"3 ":0,"F ":0}
symbol = sorted(list(grade))
for a in marks:
    a = eval(a)
    if a >= 75:
        grade["1 "] += 1
    elif a >= 70:
        grade["2+"] += 1
    elif a >= 60:
        grade["2-"] += 1
    elif a >= 50:
        grade["3 "] += 1
    else:
        grade["F "] += 1

for m in symbol:
    print(m,"|","X"*grade[m],sep='')