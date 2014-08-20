# histogram repreenting a list of marks
# Conor O'Sullivan
# 22/04/2014


"""Write a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT:

fail < 50%
50% <= 3rd < 60%
60% <= lower 2nd < 70%
70% <= upper 2nd < 75%
1st >= 75%
From the given marks, count the number of marks that satisfy the conditions of each category. For example, for the following list of marks: 32 67 54 90 77, there is one fail, one 3rd, one lower 2nd, no upper 2nds and two firsts. Then print out horizontal bars, using "X", that correspond to the counters, along with some hard-coded axes and labels to represent a histogram.

You should use an array/list to store the counters.

Sample I/O:

Enter a space-separated list of marks:
12 23 34 45 56 67 78 89 90
1 |XXX
2+|
2-|X
3 |X
F |XXXX"""

#Get list of marks
marks = (input("Enter a space-separated list of marks:\n")).split()

#Count marks
lib_marks = { "1": 0, "2+": 0, "2-":0, "3":0, "F":0}

for mark in marks:
       mark = int(mark)
       if mark < 50: 
              lib_marks["F"] += 1
       elif 50<= mark < 60:
              lib_marks["3"] += 1
       elif 60<= mark < 70:
              lib_marks["2-"] += 1
       elif 70<= mark < 75:
              lib_marks["2+"] += 1
       else: lib_marks["1"] +=1

# Display histogram
list_marks= ["1", "2+", "2-", "3", "F"]
for x in list_marks:
       axis = "{0:<2}|".format(x) 
       print(axis + "X"*lib_marks[x])
