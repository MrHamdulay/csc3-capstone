"""program to indicate the level of a set of marks
yasha longstaff 
23 april 2014"""

marks = input('Enter a space-separated list of marks:\n')
individ_marks = marks.split()
fail = 0
third = 0
low_2 = 0
up_2 = 0
first = 0
for i in individ_marks:
    i = int(i)
    if i < 50:
        fail +=1
    elif 50 <= i < 60:
        third +=1
    elif 60 <= i < 70:
        low_2 +=1
    elif 70 <= i < 75:
        up_2 +=1
    else:
        first +=1

print('1 |', 'X'*first, sep = '')
print('2+|', 'X' * up_2, sep = '')
print('2-|', 'X'* low_2, sep = '')
print('3 |', 'X'* third, sep = '')
print('F |', 'X'*fail, sep = '')