# Assignment 9 question 1
# Amy Brodie
# 11/05/2014


# initialise variables and get input
import math
students_list = []
marks_list = []
sum_m = 0
s_deviation = 0
filename = input("Enter the marks filename:\n")

# calculate the mark minus the average
def mark_minus_avg(x,u,n,c):
    if c == n:
        return 0
    else:
        return (x[c]-u)**2 + mark_minus_avg(x,u,n,c+1) 


# read lines from textfile
marks = open(filename,"r")
students_list = marks.readlines()    
marks.close


count = len(students_list)

# edit list into a list of students and a list of marks and calculate the sum of the marks
for i in range(count):
    posnl = students_list[i].find("\n")
    posc = students_list[i].find(",")
    if posnl>=0:
        marks_list.append(eval(students_list[i][posc+1:posnl]))
    else:
        marks_list.append(eval(students_list[i][posc+1:]))
    students_list[i] = students_list[i][:posc] 
    sum_m += marks_list[i]
    

# calculate average and standard deviation
if count:
    average = sum_m / count
    s_deviation = math.sqrt(mark_minus_avg(marks_list,average,count,0)/count)
else:
    average = 0
    s_deviation = 0

# print outputs 
print("The average is:", "{0:<5.2f}".format(average))
print("The std deviation is:", "{0:<4.2f}".format(s_deviation))
if s_deviation != 0:
    print("List of students who need to see an advisor:")

for i in range(count):
    if marks_list[i] < (average - s_deviation):
        print(students_list[i])