#A program that takes in a list of marks and outputs a histogram representation of the marks according to the mark categories at UCT
#Author: Emiel Zyde
#Date: 20 April 2012 

#prompt the user to enter a set of marks
marks = input("Enter a space-separated list of marks:\n")
marks = marks.split(" ")

#initialize the counters
count_fail = []
count_3 = []
count_l2 = []
count_u2 = []
count_1 = []

#scan through the marks to see which category the mark falls into
for i in marks:
    if int(i) >= 75:
        count_1.append("X")
    elif 70 <= int(i) < 75:
        count_u2.append("X")
    elif 60 <= int(i) < 70:
        count_l2.append("X")
    elif 50 <= int(i) < 60:
        count_3.append("X")
    else:
        count_fail.append("X")

#print the histogram out 
print("1 |", "".join(count_1), sep = "")
print("2+|", "".join(count_u2), sep = "")
print("2-|", "".join(count_l2), sep = "")
print("3 |", "".join(count_3), sep = "")
print("F |", "".join(count_fail), sep = "")
