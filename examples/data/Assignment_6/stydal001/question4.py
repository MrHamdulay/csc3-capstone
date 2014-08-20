# Program that prints histogram representation of marks
# Dalise Steynfaard
# STYDAL001
# 26 April 2014

def histogram():
    categories = {'1':'', '2+':'', '2-':'', '3':'', 'F':''}
    
    marks = input("Enter a space-separated list of marks:\n").split(' ')
    
    for mark in marks:
        mark = eval(mark)
        if 0 <= mark < 50:
            categories['F'] += 'X'
        elif 50 <= mark < 60:
            categories['3'] += 'X'
        elif 60 <= mark < 70:
            categories['2-'] += 'X'
        elif 70 <= mark < 75:
            categories['2+'] += 'X'
        elif 75 <= mark <= 100:
            categories['1'] += 'X'
    
    print('1 |' + categories['1'])
    print('2+|' + categories['2+'])
    print('2-|' + categories['2-'])
    print('3 |' + categories['3'])
    print('F |' + categories['F'])

histogram()