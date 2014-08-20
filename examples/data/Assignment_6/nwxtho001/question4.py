'''prints a histogram of marks attained
tome new
2014/04/21'''

markfrq = {'1': 0, '2+': 0, '2-': 0, '3': 0, 'F': 0}

marks = input ('Enter a space-separated list of marks:\n')
if marks != '':
    marks = marks.split (' ')
    marks = [eval (mark) for mark in marks]

    for mark in marks:
        if mark >= 75:
            markfrq ['1'] += 1
        elif mark >= 70:
            markfrq ['2+'] += 1
        elif mark >= 60:
            markfrq ['2-'] += 1
        elif mark >= 50:
            markfrq ['3'] += 1  
        else:
            markfrq ['F'] += 1
        
print ('1 |', 'X' * markfrq ['1'], sep = '')
print ('2+|', 'X' * markfrq ['2+'], sep = '')
print ('2-|', 'X' * markfrq ['2-'], sep = '')
print ('3 |', 'X' * markfrq ['3'], sep = '')
print ('F |', 'X' * markfrq ['F'], sep = '')