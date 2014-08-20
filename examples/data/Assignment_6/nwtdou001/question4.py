'''NWTDOU001
question4.py
25 april 2014'''

# set up a dictionary to hold number of marks in each category
cats = {'1 ':0,'2+':0,'2-':0,'3 ':0,'F ':0}

# get the marks from the user and convert to array of strings
marks = input('Enter a space-separated list of marks:\n')
marks = marks.split(' ')

# 'eval' each string to a number in array, then check in which category it falls
# then increment the corresponding dictionary value
for i in range(len(marks)):
    mark = eval(marks[i])
    if mark>=75:
        cats['1 '] += 1
    elif mark>=70:
        cats['2+'] += 1
    elif mark>=60:
        cats['2-'] += 1
    elif mark>=50:
        cats['3 '] += 1
    else:
        cats['F '] += 1

# print out each category and number of Xs according to the dictionary value
for key in sorted(cats.keys()):
    bar = 'X'*cats[key]
    print(key,'|',bar,sep='')