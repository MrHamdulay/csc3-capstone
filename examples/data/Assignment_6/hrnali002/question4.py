"""A program to output a histogram from a list of marks
Alison Hoernle
HRNALI002
20 April 2014"""

# get input list of marks
marks_str = input("Enter a space-separated list of marks:\n")
marks = marks_str.split(" ")

# introduce the initial count for each section
count_firsts = 0
count_up_sec = 0
count_low_sec = 0
count_thirds = 0
count_fail = 0

# iterate through list of marks and determine the number of marks in each category
for mark in marks:
    if eval(mark) >= 75:
        count_firsts += 1
    elif 70 <= eval(mark) < 75:
        count_up_sec += 1
    elif 60 <= eval(mark) < 70:
        count_low_sec += 1
    elif 50 <= eval(mark) < 60:
        count_thirds += 1
    else:
        count_fail += 1
        
# print the section name, the axis, and an 'X' for each mark in that category
print('1 |', 'X'* count_firsts, sep = '')
print('2+|', 'X'* count_up_sec, sep = '') 
print('2-|', 'X'* count_low_sec, sep = '')
print('3 |', 'X'* count_thirds, sep = '')
print('F |', 'X'* count_fail, sep = '')