"""takes marks as input from user and plots a histogram
Jonathan Nathan
20 April 2014"""

# gets marks from user, and creates a list of these marks
marks_input = input("Enter a space-separated list of marks:\n")
marks_list = marks_input.split(' ')

# creates counting variables for the various mark classes
firsts = 0
upper_seconds = 0
lower_seconds = 0
thirds = 0
fails = 0

# checks which class each of the marks in the marks_list fall into, and counts how many marks fall into each of the mark classes
for mark in range(len(marks_list)):
    # interprets the marks as integers, rather than strings
    if eval(marks_list[mark]) >= 75:
        firsts += 1
    elif 70 <= eval(marks_list[mark]) < 75:
        upper_seconds += 1
    elif 60 <= eval(marks_list[mark]) < 70:
        lower_seconds += 1
    elif 50 <= eval(marks_list[mark]) <60:
        thirds += 1
    else: fails += 1
    
# prints the histogram
print('1 |', 'X'*firsts, sep='')
print('2+|', 'X'*upper_seconds, sep='')
print('2-|', 'X'*lower_seconds, sep='')
print('3 |', 'X'*thirds,sep='')
print('F |', 'X'*fails,sep='')