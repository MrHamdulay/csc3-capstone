'''program to print histogram representation of marks
nasreen hoosain
27/04/14'''

#get marks and put in list
list_of_marks = input('Enter a space-separated list of marks:\n').split(' ')
#count marks per category using dictionary
counters = {'F': 0, '3': 0, '2-': 0, '2+': 0, '1': 0}
for mark in list_of_marks:
    if eval(mark) < 50:
        counters['F'] += 1
    elif 50 <= eval(mark) < 60:
        counters['3'] += 1
    elif 60 <= eval(mark) < 70:        
        counters['2-'] += 1
    elif 70 <= eval(mark) < 75:        
        counters['2+'] += 1
    else:
        counters['1'] += 1        

#print histogram in format
a = '{0:<2}{1:^}{2:<}'
print(a.format('1', '|', 'X'*int(counters['1'])))
print(a.format('2+', '|', 'X'*int(counters['2+'])))
print(a.format('2-', '|', 'X'*int(counters['2-'])))
print(a.format('3', '|', 'X'*int(counters['3'])))
print(a.format('F', '|', 'X'*int(counters['F'])))